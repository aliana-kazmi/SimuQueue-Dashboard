
function simulationDeptChart() {

  const avgSimulationDeptChart = document.getElementById('avg-time-depts-chart');
  new Chart(avgSimulationDeptChart, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'Avg wait time',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

function simulationpatientChart() {
  
  const avgSimulationPatientChart = document.getElementById('avg-time-patients-chart');
  new Chart(avgSimulationPatientChart, {
    type: 'line',
    data: {
      labels: ['Aug', 'Sept', 'Oct', 'Nov', 'Dec', 'Jan'],
      datasets: [{
      label: 'My First Dataset',
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero:true
        }
      }
    }
  });

}

simulationpatientChart()
simulationDeptChart()