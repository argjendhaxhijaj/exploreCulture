import React, { useState, useEffect } from 'react'
import { CardDeck, Card, Button, Row, Modal } from 'react-bootstrap';
import Ciftelia from './Ciftelia';
import Cifteli from './Cifteli';

function ARCategory(props) {

    const [lgShow, setLgShow] = useState(false);
    const [cardid, setCardid] = useState({});

    return (
        <React.Fragment>

        <div className="arcategorycontainer">
            
            <h2>Augmented Reality - 3D</h2>

            <div className="arcategorycardscontainer">
            
            <CardDeck>

                {props.arone.map((item, key) => {
                return <Card key={key} style={{ width: '22rem' }}>
                    <Card.Img variant="top" src={item.arimg} />
                    <Card.Body>
                        <Card.Title>{item.title}</Card.Title>
                        <Card.Text>
                        <div className="card-container">
                        {item.content}
                        </div>
                        </Card.Text>
                        <Button variant="primary" onClick={() => { setLgShow(true); setCardid(item) }}>More details</Button>
                    </Card.Body>
                </Card>
                })}

            </CardDeck>

            <Modal
                key={cardid.id}
                size="lg"
                show={lgShow}
                onHide={() => setLgShow(false)}
                aria-labelledby="example-modal-sizes-title-lg"
            >
            <Modal.Header closeButton>
                <Modal.Title id="example-modal-sizes-title-lg">
                    Augmented Reality - 3D
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <img src={cardid.arimg} style={{ width: '100%' }} id='view360img' className='img-fluid' />
                <h2 id='view360modaltitle'>{cardid.title}</h2>
                <p id='view360modaldescription'>{cardid.content}</p>
                <Cifteli arfile={cardid.arfile} />
                <p id='view360imgcredits'>{cardid.poster}</p>
            </Modal.Body>
            </Modal>

            </div>

        </div>
        
        </React.Fragment>
    )
}

export default ARCategory
