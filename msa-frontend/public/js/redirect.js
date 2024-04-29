// 페이지 리디렉션 자바스크립트
// 할인적용 페이지
const PageButton1 = document.getElementById('discountPage');
// const userid = document.querySelector('#userid');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
PageButton1.addEventListener('click', function() {
    // 페이지를 사용내역 페이지로 리디렉션합니다.
    window.location.href = './discount';
})

// 시간대검색 페이지
const PageButton2 = document.getElementById('byTimePage');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
PageButton2.addEventListener('click', function() {
    // 페이지를 시간대검색 페이지로 리디렉션합니다.
    window.location.href = '#';
})

// 사용내역 페이지
const PageButton3 = document.getElementById('logPage');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
PageButton3.addEventListener('click', function() {
    // 페이지를 사용내역 페이지로 리디렉션합니다.
    window.location.href = './coupon';
})

// 사용집계 페이지
const PageButton4 = document.getElementById('summaryPage');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
PageButton4.addEventListener('click', function() {
    // 페이지를 사용내역 페이지로 리디렉션합니다.
    window.location.href = './summary';
})

// 로그아웃
const logoutButton = document.getElementById('logOut');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
logoutButton.addEventListener('click', function() {
    // 페이지를 사용내역 페이지로 리디렉션합니다.
    //window.location.href = './logout';
    window.location.href = '../login.html';
})

// 회원정보수정 페이지
const mypageButton = document.getElementById('summaryPage');

// 버튼에 클릭 이벤트 리스너를 추가합니다.
mypageButton.addEventListener('click', function() {
    // 페이지를 사용내역 페이지로 리디렉션합니다.
    window.location.href = './mypage';
})