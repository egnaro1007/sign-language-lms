<script>
  import Icon from '@iconify/svelte';
</script>

<nav class="navbar">
      <div class="navbar__logo">
        <a href="/study"
          ><img src="/images/logo.png" alt="logo" width="120px"
        /></a>
      </div>
      <ul class="navbar__menu">
        <li class="navbar__item"><Icon icon="fluent-color:home-20" width="40px" /> Home</li>
        <li class="navbar__item"><Icon icon="fluent-emoji:open-book" width="40px" /> Luyện Tập</li>
        <li class="navbar__item"><Icon icon="mdi:account" color="pink" width="40px"/> Tài khoản</li>
        <li class="navbar__item"><Icon icon="mdi:cog" color="gray" width="40px" /> Cài đặt</li>
      </ul>
    </nav>
<div class="divider">
  <div class="content">
    <slot />
  </div>
  <aside class="sidebar">
    <div class="sidebar__card">
      <h2>Bạn biết không</h2>
      <p>
        Vẻ đẹp của giao tiếp không nằm ở âm thanh, mà nằm ở sự kết nối giữa
        những trái tim.
      </p>
    </div>
    <div class="sidebar__card">
      <h2>Nhiệm vụ hằng ngày</h2>
      <p>Kiếm 10 KN</p>
      <a href="/study">Xem Tất Cả</a>
    </div>
  </aside>
</div>
