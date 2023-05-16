window.colordet = async () => {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-right',
      iconColor: 'white',
      customClass: {
        popup: 'colored-toast'
      },
      showConfirmButton: false,
      timer: 6600,
      timerProgressBar: true
    })
    await Toast.fire({
      icon: 'info',
      title: "Hola Gente Hermosa ✌️!"
    })
    }
