<script>
  let isZoomed = false;

  function toggleZoom() {
    isZoomed = !isZoomed;
  }
</script>

<style lang="scss">
  .video-card {
    position: relative;
    width: 300px;
    height: 400px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.3s ease;

    video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: all 0.3s ease;
    }

    &.zoomed {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(1.5);
      z-index: 1000;
      width: 80vw;
      height: 80vh;
      
      video {
        width: 100%;
        height: 100%;
        object-fit: contain;
      }
    }
  }
</style>

<div 
  class="video-card {isZoomed ? 'zoomed' : ''}"
  on:click={toggleZoom}
>
  <video autoplay loop muted>
    <source src="/video.mp4" type="video/mp4" />
  </video>
</div>