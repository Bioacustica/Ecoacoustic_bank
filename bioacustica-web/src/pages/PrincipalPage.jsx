import React from 'react'
import Fab from '@material-ui/core/Fab'
import 'bootstrap-css-only/css/bootstrap.min.css';
import PersonAdd from '@material-ui/icons/PersonAdd';
import LabelIcon from '@material-ui/icons/Label';
import Backup from '@material-ui/icons/Backup';
import CloudDownloadIcon from '@material-ui/icons/CloudDownload';
import MusicNoteIcon from '@material-ui/icons/MusicNote';
import Cookies from 'universal-cookie'


const cookies = new Cookies()

const PrincipalPage = () => {
    const name = cookies.get('name')
    const token = window.localStorage.getItem("token")
    const rol = cookies.get('rol')

    const cerrarSesion = () => {
        // Aca se borrar las cookies :"v
        cookies.remove('username', { path: "/" })
        cookies.remove('rol', { path: "/" })
        window.localStorage.clear()
        window.location.href = './'
    }


    return (
        <>
            <div className='btn-group-vertical btnfloating' style={{ position: "fixed", height: '550px' }}>

                <Fab color='primary' aria-label='agregar'>
                    <PersonAdd />
                </Fab>
                <br />
                <Fab color='inherit' aria-label='editar'>
                    <MusicNoteIcon />
                </Fab>
                <br />
                <Fab color='secondary' aria-label='agregar'>
                    <Backup />
                </Fab>
                <br />
                <Fab color='default' aria-label='agregar'>
                    <LabelIcon />
                </Fab>
                <br />
                <Fab color='secondary' aria-label='agregar'>
                    <CloudDownloadIcon />
                </Fab>
            </div>
            <header>
                {/* Navbar */}
                <nav className="navbar navbar-expand-lg navbar-light bg-white">
                    <div className="container-fluid">
                        <button className="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarExample01" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
                            <i className="fas fa-bars" />
                        </button>
                        <div className="collapse navbar-collapse" id="navbarExample01">
                            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                                <li className="nav-item active">
                                    <label className="nav-link" aria-current="page" >Bienvenido {name}</label>
                                </li>
                                <li className="nav-item">
                                    <label className="nav-link" > Tiene el rol de {rol} papaaa</label>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                {/* Navbar */}
                {/* Background image */}
                <div className="p-5  bg-image" style={{ backgroundImage: 'url("https://mdbcdn.b-cdn.net/img/new/slides/041.jpg")', height: '400px' }}>
                    <div className="mask" style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }}>
                        <div className="d-flex justify-content-center align-items-center h-100">
                            <div className="text-white">
                               
                                <h4 className="mb-3">Alabado sea el señor</h4>
                                <button className="btn btn-outline-light btn-lg"
                                    onClick={() => cerrarSesion()} >Salir</button>
                            </div>
                        </div>
                    </div>
                </div>
                {/* Background image */}
            </header>
            {// Papi aca empiezan los botones
            }
            
        </>
    )
}

export default PrincipalPage
