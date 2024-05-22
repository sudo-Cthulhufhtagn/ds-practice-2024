import { Link } from "react-router-dom";

export const Heros = () => {

    return (
        <div>
            <div className='d-none d-lg-block'>
                <div className='row g-0 mt-5'>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-left'></div>
                    </div>
                    <div className='col-4 col-md-4 container d-flex justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Ignite Your Imagination with Our Best events!</h1>
                            <p className='lead'>
                                We believe there's an event for everyone. Whether you're a seasoned professional or just starting out,
                                we have the perfect event for you. Join us and meet like-minded people who share your passion.
                            </p>
                                <Link type='button' className='btn btn-outline-success' to='/search'>
                                    Explore books</Link>
                        </div>
                    </div>
                </div>
                <div className='row g-0'>
                    <div className='col-4 col-md-4 container d-flex 
                        justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Every event matters</h1>
                            <p className='lead'>
                                We believe that every event is important. Whether you're attending a small gathering or a large conference,
                                we want to make sure you have the best experience possible. That's why we work hard to bring you the best events
                                from around the world.
                            </p>
                        </div>
                    </div>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-right'></div>
                    </div>
                </div>
            </div>

            {/* Mobile Heros */}
            <div className='d-lg-none'>
                <div className='container'>
                    <div className='m-2'>
                        <div className='col-image-left'></div>
                        <div className='mt-2'>
                            <h1>What have you been reading?</h1>
                            <p className='lead'>
                                The library team would love to know what you have been reading.
                                Whether it is to learn a new skill or grow within one,
                                we will be able to provide the top content for you!
                            </p>
                                <Link type='button' className='btn main-color btn-lg text-white'
                                    to='search'>Explore top books</Link>
                        </div>
                    </div>
                    <div className='m-2'>
                        <div className='col-image-right'></div>
                        <div className='mt-2'>
                            <h1>Our collection is always changing!</h1>
                            <p className='lead'>
                                
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}