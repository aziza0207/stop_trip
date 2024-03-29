import { useState } from 'react';
import { ArrowRight } from '../../shared/ui/icons/icons-tools/ArrowRight';
import './popularCategories.scss';
import { AllCategories, ModalWindow } from '../../entities/controls';
import { categories } from '../../shared/const/categories';
import { useNavigate } from 'react-router-dom';
import { useMatchMedia } from '../../app/hooks/useMatchMedia';
import { useGetAdvertsQuery } from '../../app/api/fetchAdverts';
import { getSpelling } from './libr/getSpelling';

export const PopularCategories = () => {
    const [showModal, setShowModal] = useState(false);
    const navigate = useNavigate();
    const { isMobile } = useMatchMedia();
    const { data = [] } = useGetAdvertsQuery('');

    return (
        <div className="popular-categories">
            <div className="popular-categories-wrapper">
                <div className="categories-titles">
                    <h3>Популярные категории</h3>
                    {isMobile && (
                        <>
                            <AllCategories
                                showModal={showModal}
                                setShowModal={setShowModal}
                            />
                            <ModalWindow
                                showModal={showModal}
                                setShowModal={setShowModal}
                            />
                        </>
                    )}
                </div>

                <div className="categories-list">
                    {Object.entries(categories)
                        .filter((el) => el[0] !== 'event')
                        .map((el) => {
                            const { icon: Icon } = el[1];
                            const offersAmount = data.filter((item) => item.category === el[0]).length;
                            return (
                                <div
                                    key={el[0]}
                                    className={`category ${el[0]}>`}
                                    onClick={() => navigate(`/${el[0]}`)}
                                >
                                    <Icon />
                                    <p>{el[1].description}</p>
                                    <span>
                                        {`${offersAmount} ${getSpelling(offersAmount)} `}
                                        <ArrowRight color="#1F6FDE" />
                                    </span>
                                </div>
                            );
                        })}
                </div>
            </div>
        </div>
    );
};
