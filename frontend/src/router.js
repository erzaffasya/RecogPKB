import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
        component: () =>
            import('@/views/Index'),
        children: [
            // Dashboard
            {
                name: 'Data Absen',
                path: '',
                redirect: 'data-absen',
            },
            {
                name: 'Data Absen',
                path: 'data-absen',
                component: () =>
                    import('@/views/DataAbsen'),
            },
            {
                name: 'Data Mahasiswa',
                path: 'mahasiswa',
                component: () =>
                    import('@/views/DataMahasiswa'),
            },
            {
                name: 'Tambah Data Mahasiswa',
                path: 'tambah-mahasiswa',
                component: () =>
                    import('@/views/TambahMahasiswa'),
            },
            {
                name: 'Create Report',
                path: 'create-report',
                component: () =>
                    import('@/views/CreateReport'),
            },
        ],
    },
    ],
})