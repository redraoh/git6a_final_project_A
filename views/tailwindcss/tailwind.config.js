/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}

// /* gpt 참조 */
// /** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: ["../templates/**/*.html"],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
//   corePlugins: {
//     preflight: false, // Tailwind의 기본 스타일 제거
//     container: false, // 컨테이너 기능 비활성화
//     accessibility: false, // 접근성 기능 비활성화
//   },
// }


