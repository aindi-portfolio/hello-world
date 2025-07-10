import Header from '../components/Header';
import '../styles/HomePage.css';

export default function HomePage() {
    return (
        <>
            <Header />
            <div className="grid-container">
                <div className="grid-item">1</div>
                <div className="grid-item">2</div>
                <div className="grid-item">3</div>
                <div className="grid-item">4</div>
            </div>
        </>
    )
}