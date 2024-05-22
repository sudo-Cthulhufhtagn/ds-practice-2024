import { Link } from "react-router-dom";

export const ExploreTopBooks = () => {
    return (
        <div className='p-5 mb-4 bg-dark header'>
            <div className='container-fluid py-5 text-white 
                d-flex justify-content-center align-items-center'>
                <div>
                    <h1 className='display-5 fw-bold'>Explore next wonderful event!</h1>
                    <p className='col-md-8 fs-4'>Meet the people and enjoy the atmoshphere</p>
                    <Link type='button' className='btn btn-outline-success' to='/search'>
                        To events</Link>
                </div>
            </div>
        </div>
    );
}