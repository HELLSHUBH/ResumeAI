const historyContainer = document.getElementById('historyContainer');

function requireLogin() {
    const userId = localStorage.getItem('user_id');

    if (!userId) {
        alert('Please login first.');
        window.location.href = 'Home.html';
        return false;
    }

    return true;
}

function getUserType() {
    return localStorage.getItem('user_type');
}

function getUserId() {
    return localStorage.getItem('user_id');
}

async function loadHistory() {
    if (!requireLogin()) {
        return;
    }

    const userType = getUserType();

    if (userType === 'recruiter' || userType === 'employer') {
        await loadRecruiterJobs();
    } else {
        await loadApplicantHistory();
    }
}

async function loadApplicantHistory() {
    const userId = getUserId();

    try {
        historyContainer.innerHTML = `
            <div class="card p-4 text-center">
                <p class="text-secondary mb-0">Loading applicant history...</p>
            </div>
        `;

        const response = await fetch(`http://localhost:3000/api/history/${userId}`);
        const data = await response.json();

        if (!response.ok) {
            showError(data.message || 'Could not load history.');
            return;
        }

        if (!data.history || data.history.length === 0) {
            historyContainer.innerHTML = `
                <div class="card p-4 text-center">
                    <h5 class="fw-bold">No analysis history found</h5>
                    <p class="text-secondary mb-0">Your generated resume reports will appear here.</p>
                </div>
            `;
            return;
        }

        historyContainer.innerHTML = '';

        data.history.forEach(item => {
            const card = document.createElement('div');
            card.className = 'card shadow-sm border-0 p-4 mb-3';

            card.innerHTML = `
                <div class="d-flex justify-content-between align-items-start gap-3 flex-wrap">
                    <div>
                        <h5 class="fw-bold mb-1">${item.resume_file_name || 'Resume Analysis'}</h5>

                        <p class="text-secondary small mb-2">
                            Generated on: ${item.generated_at || '-'}
                        </p>

                        <p class="mb-1">
                            <strong>Matched Skills:</strong> ${formatList(item.matched_skills)}
                        </p>

                        <p class="mb-1">
                            <strong>Missing Skills:</strong> ${formatList(item.missing_skills)}
                        </p>

                        <p class="mb-1">
                            <strong>Feedback:</strong> ${formatList(item.feedback)}
                        </p>

                        <p class="mb-1">
                            <strong>Suggestions:</strong> ${formatList(item.suggestions)}
                        </p>
                    </div>

                    <div class="text-end">
                        <h2 class="fw-bold text-warning mb-0">${item.match_score || 0}%</h2>
                        <span class="badge bg-dark">Match Score</span>
                    </div>
                </div>
            `;

            historyContainer.appendChild(card);
        });

    } catch (error) {
        console.error('Applicant history error:', error);
        showError('Could not connect to server.');
    }
}

async function loadRecruiterJobs() {
    const recruiterId = getUserId();

    try {
        historyContainer.innerHTML = `
            <div class="card p-4 text-center">
                <p class="text-secondary mb-0">Loading recruiter history...</p>
            </div>
        `;

        const response = await fetch(`http://localhost:3000/api/recruiter/history/${recruiterId}`);
        const data = await response.json();

        if (!response.ok) {
            showError(data.message || 'Could not load recruiter history.');
            return;
        }

        if (!data.jobs || data.jobs.length === 0) {
            historyContainer.innerHTML = `
                <div class="card p-4 text-center">
                    <h5 class="fw-bold">No recruiter history found</h5>
                    <p class="text-secondary mb-0">Your ranked applicant reports will appear here.</p>
                </div>
            `;
            return;
        }

        historyContainer.innerHTML = `
            <div class="mb-3">
                <p class="text-secondary small mb-1">RECRUITER HISTORY</p>
                <h4 class="fw-bold">Screened Job Roles</h4>
                <p class="text-secondary mb-0">
                    Click a job title to view applicant ranking reports.
                </p>
            </div>
        `;

        data.jobs.forEach(job => {
            const card = document.createElement('div');
            card.className = 'card shadow-sm border-0 p-4 mb-3';

            card.innerHTML = `
                <div class="d-flex justify-content-between align-items-center gap-3 flex-wrap">
                    <div>
                        <h5 class="fw-bold mb-1">${job.job_title}</h5>
                        <p class="text-secondary small mb-1">
                            Generated on: ${job.generated_at || '-'}
                        </p>
                        <p class="mb-0">
                            <strong>Total Applicants:</strong> ${job.total_applicants}
                            |
                            <strong>Top Score:</strong> ${job.top_score}%
                        </p>
                    </div>

                    <button class="btn btn-warning fw-semibold view-job-btn" data-job-id="${job.job_id}">
                        View Reports
                    </button>
                </div>

                <div class="job-report-box mt-3 d-none" id="jobReportBox-${job.job_id}">
                    <p class="text-secondary mb-0">Loading reports...</p>
                </div>
            `;

            historyContainer.appendChild(card);
        });

        addJobViewButtonEvents();

    } catch (error) {
        console.error('Recruiter history error:', error);
        showError('Could not connect to server.');
    }
}

function addJobViewButtonEvents() {
    const buttons = document.querySelectorAll('.view-job-btn');

    buttons.forEach(button => {
        button.addEventListener('click', async () => {
            const jobId = button.getAttribute('data-job-id');
            const reportBox = document.getElementById(`jobReportBox-${jobId}`);

            if (!reportBox) {
                return;
            }

            if (!reportBox.classList.contains('d-none')) {
                reportBox.classList.add('d-none');
                button.textContent = 'View Reports';
                return;
            }

            reportBox.classList.remove('d-none');
            button.textContent = 'Hide Reports';

            await loadRecruiterJobReports(jobId, reportBox);
        });
    });
}

async function loadRecruiterJobReports(jobId, reportBox) {
    try {
        reportBox.innerHTML = `
            <p class="text-secondary mb-0">Loading reports...</p>
        `;

        const response = await fetch(`http://localhost:3000/api/recruiter/history/job/${jobId}`);
        const data = await response.json();

        if (!response.ok) {
            reportBox.innerHTML = `
                <p class="text-danger mb-0">${data.message || 'Could not load reports.'}</p>
            `;
            return;
        }

        const reports = data.reports || [];

        if (reports.length === 0) {
            reportBox.innerHTML = `
                <p class="text-secondary mb-0">No applicant reports found for this job.</p>
            `;
            return;
        }

        let tableRows = '';

        reports.forEach((report, index) => {
            tableRows += `
                <tr>
                    <td class="fw-bold">#${index + 1}</td>

                    <td>
                        <div class="fw-semibold">${report.resume_file_name || 'Applicant Resume'}</div>
                        <div class="small text-secondary">Applicant Resume</div>
                    </td>

                    <td>
                        <span class="badge ${getScoreClass(report.match_score)}">
                            ${report.match_score}%
                        </span>
                    </td>

                    <td>${formatSkillBadges(report.matched_skills)}</td>

                    <td>${formatSkillBadges(report.missing_skills)}</td>

                    <td>
                        <span class="badge ${getStatusClass(report.match_score)}">
                            ${report.status || getStatusText(report.match_score)}
                        </span>
                    </td>
                </tr>
            `;
        });

        reportBox.innerHTML = `
            <div class="table-responsive">
                <table class="table table-hover align-middle">
                    <thead class="table-dark">
                        <tr>
                            <th>Rank</th>
                            <th>Applicant</th>
                            <th>Match Score</th>
                            <th>Matched Skills</th>
                            <th>Missing Skills</th>
                            <th>Status</th>
                        </tr>
                    </thead>

                    <tbody>
                        ${tableRows}
                    </tbody>
                </table>
            </div>
        `;

    } catch (error) {
        console.error('Recruiter job report error:', error);

        reportBox.innerHTML = `
            <p class="text-danger mb-0">Could not connect to server.</p>
        `;
    }
}

function formatList(value) {
    if (!value || value.length === 0) {
        return '-';
    }

    if (Array.isArray(value)) {
        return value.join(', ');
    }

    return value;
}

function formatSkillBadges(skills) {
    if (!skills || skills.length === 0) {
        return '<span class="text-secondary small">None</span>';
    }

    return skills.slice(0, 6).map(skill => {
        return `<span class="badge text-bg-light border me-1 mb-1">${skill}</span>`;
    }).join('');
}

function getScoreClass(score) {
    if (score >= 80) {
        return 'text-bg-success';
    }

    if (score >= 60) {
        return 'text-bg-warning';
    }

    return 'text-bg-danger';
}

function getStatusClass(score) {
    if (score >= 80) {
        return 'text-bg-success';
    }

    if (score >= 60) {
        return 'text-bg-warning';
    }

    return 'text-bg-danger';
}

function getStatusText(score) {
    if (score >= 80) {
        return 'Shortlist';
    }

    if (score >= 60) {
        return 'Review';
    }

    return 'Reject';
}

function showError(message) {
    historyContainer.innerHTML = `
        <div class="card p-4 text-center">
            <p class="text-danger mb-0">${message}</p>
        </div>
    `;
}

loadHistory();