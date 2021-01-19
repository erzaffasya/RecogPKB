import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
        component: () =>
            import ('@/views/Index'),
        children: [
            // Dashboard
            {
                name: 'Attendance List',
                path: '',
                redirect: 'data-absen',
            },
            {
                name: 'Data Absen',
                path: 'data-absen',
                component: () =>
                    import ('@/views/DataAbsen'),
            },
            {
                name: 'Data Mahasiswa',
                path: 'mahasiswa',
                component: () =>
                    import ('@/views/DataMahasiswa'),
            },
            {
                name: 'Tambah Data Mahasiswa',
                path: 'tambah-mahasiswa',
                component: () =>
                    import ('@/views/TambahMahasiswa'),
            },
            {
                name: 'Create Report',
                path: 'create-report',
                component: () =>
                    import ('@/views/CreateReport'),
            },
            {
                name: 'Notifications',
                path: 'components/notifications',
                component: () =>
                    import ('@/views/dashboard/component/Notifications'),
            },
            {
                name: 'Icons',
                path: 'components/icons',
                component: () =>
                    import ('@/views/dashboard/component/Icons'),
            },
            {
                name: 'Typography',
                path: 'components/typography',
                component: () =>
                    import ('@/views/dashboard/component/Typography'),
            },
            // Tables
            {
                name: 'Regular Tables',
                path: 'tables/regular-tables',
                component: () =>
                    import ('@/views/dashboard/tables/RegularTables'),
            },
            // Maps
            {
                name: 'Google Maps',
                path: 'maps/google-maps',
                component: () =>
                    import ('@/views/dashboard/maps/GoogleMaps'),
            },
            // Upgrade
            {
                name: 'Upgrade',
                path: 'upgrade',
                component: () =>
                    import ('@/views/dashboard/Upgrade'),
            },
        ],
    }, ],
})