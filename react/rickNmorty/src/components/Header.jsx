// Connected to the HomePage.jsx //
import NavBar from "./NavBar"
import '../styles/Header.css';

export default function Header() {
    return (
        <>
            <div className="container">
                <h1 className="mb-3">
                    Welcome to the Rick and Morty Universe
                </h1>
                <NavBar />
            </div>
        </>
    )
}