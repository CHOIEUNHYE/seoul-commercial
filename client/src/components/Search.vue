<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>서울 소상공인 상권 정보</h1>
        <hr><br>
      <input type="text" v-model="searchKeyword" placeholder="검색어 입력">
      <button @click="search">검색</button><br>
      <div v-if="isLoading"><br>로딩 중...</div>
      <table v-if="!isLoading" class="table table-hover">
        <thead>
            <tr>
              <th scope="col">상호명</th>
              <th scope="col">업종코드</th>
              <th scope="col">업종명</th>
              <th scope="col">지번주소</th>
              <th scope="col">도로명주소</th>
              <th scope="col">경도</th>
              <th scope="col">위도</th>
              <th></th>
            </tr>
        </thead>
        <tbody>
          <tr v-for="result in searchResults" :key="result.id">
            <td>{{ result.상호명 }}</td>
            <td>{{ result.상권업종대분류코드 }}</td>
            <td>{{ result.상권업종대분류명 }}</td>
            <td>{{ result.지번주소 }}</td>
            <td>{{ result.도로명주소 }}</td>
            <td>{{ result.경도 }}</td>
            <td>{{ result.위도 }}</td>
          </tr>
      </tbody>
    </table>
    </div>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchKeyword: '',
        searchResults: [],
        isLoading: false
      };
    },
    methods: {
      search() {
        this.isLoading = true; // 로딩 상태 설정
  
        axios.get('http://127.0.0.1:5001/search', { params: { keyword: this.searchKeyword } })
          .then(response => {
            this.searchResults = response.data;
            console.log(response.data)
          })
          .catch(error => {
            console.error('검색 결과를 가져올 수 없습니다.', error);
          })
          .finally(() => {
            this.isLoading = false; // 로딩 상태 해제
          });
      }
    }
  };
  </script>