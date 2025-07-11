import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function CharacterCard({ character }) {
  return (
    <Card style={{ width: '18rem' }} className='text-center'>
      <Card.Img variant="top" src={character.image} />
      <Card.Body>
        <Card.Title>{character.name}</Card.Title>
        <Card.Text>{character.status} - {character.species}</Card.Text>
        <Button variant="primary">More Information</Button>
      </Card.Body>
    </Card>
  );
}

export default CharacterCard;