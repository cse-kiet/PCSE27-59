/**
 * Chart.js initialization and configuration
 */

// Chart color palette
const chartColors = {
    primary: '#0d6efd',
    success: '#198754',
    warning: '#ffc107',
    danger: '#dc3545',
    info: '#0dcaf0',
    secondary: '#6c757d'
};

// Common chart options
const commonOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
        legend: {
            display: true,
            position: 'bottom',
            labels: {
                padding: 15,
                font: {
                    size: 12
                }
            }
        },
        tooltip: {
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            padding: 12,
            titleFont: {
                size: 14
            },
            bodyFont: {
                size: 13
            },
            cornerRadius: 4
        }
    }
};

/**
 * Initialize Severity Distribution Pie Chart
 */
function initializeSeverityChart(data) {
    const ctx = document.getElementById('severityChart');
    if (!ctx) return;
    
    const chartData = {
        labels: ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative'],
        datasets: [{
            data: [
                data.None || 0,
                data.Mild || 0,
                data.Moderate || 0,
                data.Severe || 0,
                data.Proliferative || 0
            ],
            backgroundColor: [
                chartColors.success,
                '#fbbf24',
                chartColors.warning,
                '#f97316',
                chartColors.danger
            ],
            borderWidth: 2,
            borderColor: '#ffffff'
        }]
    };
    
    new Chart(ctx, {
        type: 'doughnut',
        data: chartData,
        options: {
            ...commonOptions,
            cutout: '60%',
            plugins: {
                ...commonOptions.plugins,
                legend: {
                    ...commonOptions.plugins.legend,
                    position: 'right'
                },
                tooltip: {
                    ...commonOptions.plugins.tooltip,
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = total > 0 ? ((value / total) * 100).toFixed(1) : 0;
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

/**
 * Initialize Age Distribution Bar Chart
 */
function initializeAgeChart() {
    const ctx = document.getElementById('ageChart');
    if (!ctx) return;
    
    // Fetch age distribution data
    fetch('/api/dashboard-stats')
        .then(response => response.json())
        .then(data => {
            const ageData = data.age_distribution || {'18-30': 0, '31-45': 0, '46-60': 0, '60+': 0};
            
            const chartData = {
                labels: ['18-30', '31-45', '46-60', '60+'],
                datasets: [{
                    label: 'Number of Patients',
                    data: [
                        ageData['18-30'],
                        ageData['31-45'],
                        ageData['46-60'],
                        ageData['60+']
                    ],
                    backgroundColor: chartColors.primary,
                    borderColor: chartColors.primary,
                    borderWidth: 1
                }]
            };
            
            new Chart(ctx, {
                type: 'bar',
                data: chartData,
                options: {
                    ...commonOptions,
                    plugins: {
                        ...commonOptions.plugins,
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                stepSize: 1
                            },
                            grid: {
                                display: true,
                                color: 'rgba(0, 0, 0, 0.05)'
                            }
                        },
                        x: {
                            grid: {
                                display: false
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error loading age distribution:', error));
}

/**
 * Initialize Risk Level Chart
 */
function initializeRiskChart(elementId, data) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    
    const chartData = {
        labels: ['Low Risk', 'Medium Risk', 'High Risk', 'Critical'],
        datasets: [{
            data: data,
            backgroundColor: [
                chartColors.success,
                chartColors.warning,
                '#f97316',
                chartColors.danger
            ],
            borderWidth: 2,
            borderColor: '#ffffff'
        }]
    };
    
    new Chart(ctx, {
        type: 'pie',
        data: chartData,
        options: commonOptions
    });
}

/**
 * Initialize Trend Line Chart
 */
function initializeTrendChart(elementId, labels, data) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    
    const chartData = {
        labels: labels,
        datasets: [{
            label: 'Detection Rate',
            data: data,
            borderColor: chartColors.primary,
            backgroundColor: 'rgba(13, 110, 253, 0.1)',
            tension: 0.4,
            fill: true,
            pointRadius: 4,
            pointHoverRadius: 6
        }]
    };
    
    new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
            ...commonOptions,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

/**
 * Initialize Confidence Score Chart
 */
function initializeConfidenceChart(elementId, scores) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;
    
    const chartData = {
        labels: scores.map((_, i) => `Scan ${i + 1}`),
        datasets: [{
            label: 'Confidence Score',
            data: scores,
            backgroundColor: scores.map(score => 
                score >= 90 ? chartColors.success : 
                score >= 80 ? chartColors.info : 
                chartColors.warning
            ),
            borderWidth: 1,
            borderColor: '#ffffff'
        }]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            ...commonOptions,
            indexAxis: 'y',
            plugins: {
                ...commonOptions.plugins,
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
}

/**
 * Update chart with new data
 */
function updateChart(chart, newData) {
    if (!chart) return;
    
    chart.data.datasets[0].data = newData;
    chart.update('active');
}

/**
 * Destroy chart instance
 */
function destroyChart(chartInstance) {
    if (chartInstance) {
        chartInstance.destroy();
    }
}

// Export chart functions
window.chartUtils = {
    initializeSeverityChart,
    initializeAgeChart,
    initializeRiskChart,
    initializeTrendChart,
    initializeConfidenceChart,
    updateChart,
    destroyChart,
    chartColors
};