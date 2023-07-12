<template>
    <div>
      <h1 style="text-align:center;">서울시 업종 대분류별 업종 수</h1>
      <hr><br>
      <div class="category-btn" >
      <!-- 버튼마다 키속성을 다르게 둔 이유 : 각 버튼에 대한 고유한 key 값이 할당되어 캐시 무효화가 수행되는 것을 시도 -->
      <button class="btn btn-outline-dark" 
        @click="sendValue('음식')" :key="음식">음식</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('숙박')" :key="숙박">숙박</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('교육')" :key="교육">교육</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('과학·기술')" :key="과학기술">과학·기술</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('소매')" :key="소매">소매</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('시설관리·임대')" :key="시설관리임대">시설관리·임대</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('수리·개인')" :key="수리개인">수리·개인</button>
      <button class="btn btn-outline-dark" 
        @click="sendValue('부동산')" :key="부동산">부동산</button>
      </div>
      <div v-if="isLoading" class="centered"><br>로딩 중...<br></div>
      <div class="chart-container">
        <canvas id="myChart" ></canvas>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Chart from 'chart.js/auto';
  export default {
    data(){
      return {
        isLoading: false,
        음식: '음식',
        숙박: '숙박',
        교육: '교육',
        과학기술:'과학기술',
        소매:'소매',
        시설관리임대:'시설관리임대',
        수리개인:'수리개인',
        부동산:'부동산'
      };
      
    },
    mounted() {
  
    },
    methods: {
      sendValue(value) {
        this.isLoading = true; // 로딩 상태 설정
        axios.get('http://127.0.0.1:5001/chart', { params: { value: value } })
          .then(response => {
            const data = response.data;
            console.log(data);
            const transformedData = this.transformData(data);
            this.drawChart(transformedData);
          })
          .catch(error => {
            console.error('데이터를 가져올 수 없습니다.', error);
          })
          .finally(() => {
            this.isLoading = false; // 로딩 상태 해제
          });
      },
      transformData(data) {
        const labels = [];
        const values = [];
        
        for (const key in data) {
          if (data.hasOwnProperty(key)) {
            labels.push(key);
            values.push(data[key]);
          }
        }
        
        return {
          labels: labels,
          values: values
        };
      },
      drawChart(data) {
  
        const canvas = document.getElementById('myChart');
        const ctx = canvas.getContext('2d');
      
  
        new Chart(
          ctx, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              label: '업종 수',
              data: data.values,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }]
          },
          options: {
            reponsive:false,
            scales: {
              y: {
                beginAtZero: true
              }
            },
          }
        });
      }
    }
  };
  </script>
  
  <style>
  .category-btn {
    text-align: center;
  }
  
  .category-btn button {
    margin-right: 10px;
  }
  
  .centered 
  { display: table; margin-left: auto; margin-right: auto; }
  
  </style>