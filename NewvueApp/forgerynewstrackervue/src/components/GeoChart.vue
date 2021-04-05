<template>
    <div>
        <geo-chart :data="[['United States', 44], ['Germany', 23], ['Brazil', 22]]"></geo-chart>
    </div>
</template>

<script>

export default {
    name:"GeoChart",
     mounted() {
      let recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', "https://www.gstatic.com/charts/loader.js")
      document.head.appendChild(recaptchaScript)
    },
}
</script>

