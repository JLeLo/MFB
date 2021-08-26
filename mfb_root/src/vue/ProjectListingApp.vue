<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + Vite" />
</template>

<script setup>
import HelloWorld from './components/HelloWorld.vue'

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/master/active-rfcs/0040-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->


<template>
<div style="height: 100%">
    <div class="container">
        <div id="center">
            <ag-grid-vue style="width: 100%; height: 100%;"
                class="ag-theme-alpine"
                id="myGrid"
                :gridOptions="gridOptions"
                @grid-ready="onGridReady"
                :columnDefs="columnDefs"
                :rowData="rowData">
            </ag-grid-vue>
        </div>
</div>
</div>
</template>


<style lang="scss">
    @import "../../node_modules/ag-grid-community/dist/styles/ag-grid.css";
    @import "../../node_modules/ag-grid-community/dist/styles/ag-theme-alpine.css";
    
    .container {
    display: -ms-grid;
    display: grid;
    grid-template-rows: calc(100vh - 10rem);
    width: 100%;
    }

    #center {
    width: 100%;
    // overflow: hidden;
    }

</style>

<script>
    import { AgGridVue } from "ag-grid-vue3";

    export default {
        name: 'App',
        data() {
            return {
                gridOptions: null,
                gridApi: null,
                columnApi: null,
                rowData: null,
                columnDefs: null,
            }
        },
        components: {
            AgGridVue
        },
        beforeMount() {
            this.gridOptions = {};
            this.columnDefs = [
                { field: 'project_name', headerName: 'Project Name', },
                { field: 'project_date_created', headerName: 'Project Date Created',  },
                { field: 'project_date_last_executed', headerName: 'Project Date Last Executed',  },
                { field: 'project_status', headerName: 'Project Status',  },
            ];

            fetch('http://127.0.0.1:8002/all_projects/')
                .then(result => result.json())
                .then(rowData => this.rowData = rowData);
        },
        mounted(){
            this.gridApi = this.gridOptions.api;
            this.gridColumnApi = this.gridOptions.columnApi;
        },
        methods: {
            onGridReady(params) {
            params.api.sizeColumnsToFit();
            window.addEventListener('resize', function () {
                setTimeout(function () {
                params.api.sizeColumnsToFit();
                });
            });

            params.api.sizeColumnsToFit();
            },
        },
    }
</script>
