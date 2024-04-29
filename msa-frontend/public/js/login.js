const loginfrm = document.querySelector('#loginfrm');
const userid = document.querySelector('#userid');
const passwd = document.querySelector('#passwd');
// const userid = document.getElementById('userid'); // 수정된 부분
// const passwd = document.getElementById('passwd'); // 수정된 부분
const loginbtn = document.querySelector('#loginbtn');

// 로그인버튼 이벤트 추가
loginbtn.addEventListener('click', async () => {
    const res = await fetch('http://127.0.0.1:8020/login',
        {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                mid: userid.value, // 수정된 부분
                mpwd: passwd.value // 수정된 부분
            })
        });
    const data = await res.json();
    if (res.ok) {
        alert('로그인 성공!!');
    } else {
        alert('로그인 실패!!');
        console.log(data.detail);
    }
});

// loginbtn.addEventListener('click', async () => {
//     const res = await fetch('http://127.0.0.1:8020/login', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({
//             mid: userid.value,
//             mpwd: passwd.value
//         })
//     });
//     if (res.ok) {
//         const data = await res.json();
//         alert('로그인 성공!!');
//     } else {
//         const errorData = await res.json();
//         alert('로그인 실패!!');
//         console.log(errorData.detail);
//     }
// });
