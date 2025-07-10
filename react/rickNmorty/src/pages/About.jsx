import Header from "../components/Header";

export default function About() {
    return (
        <>
            <Header />
            <div className="about-page">
                <h1>About Page</h1>
                <p>This is the About page where you can find information about the Rick and Morty universe, the creators, and the inspiration behind the show.</p>
                {/* You can add more content or components related to the About section here */}
            </div>
        </>
    );
}