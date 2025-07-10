// Goes into header.jsx //


import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import '../styles/NavBar.css';

function NavBar() {
  return (
      <Container>
        <ul className="flex gap-4 m-0 p-0">
            <Link className="link" to="/">Home</Link>
            <Link className="link" to="/characters">Characters</Link>
            <Link className="link" to="/locations">Locations</Link>
            <Link className="link" to="/episodes">Episodes</Link>
            <Link className="link" to="/about">About</Link>
        </ul>
      </Container>
  );
}

export default NavBar;