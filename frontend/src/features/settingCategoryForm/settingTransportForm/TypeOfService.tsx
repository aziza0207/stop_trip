import { useEffect, useState } from 'react';
import { UseFormRegister, UseFormWatch } from 'react-hook-form';
import { ArrowDown } from '../../../shared/ui/icons/icons-tools/ArrowDown';
import { ArrowTop } from '../../../shared/ui/icons/icons-tools/ArrowTop';
import { Jackdaw } from '../../../shared/ui/icons/icons-tools/Jackdaw';
import { TypeSettingTransport } from '../../../widgets/settingForm/settingTransport/libr/TypeSettingTransport';
import { valuesOfTransportForm } from '../../../widgets/settingForm/settingTransport/libr/valuesOfTransportForm';

interface Props {
    register: UseFormRegister<TypeSettingTransport>;
    watch: UseFormWatch<TypeSettingTransport>;
}

export const TypeOfService = ({ register, watch }: Props) => {
    const typeOfService = watch('typeOfService');
    const arrOfValues = valuesOfTransportForm.typeOfService

    const [showDropDown, setShowDropDown] = useState(false);

    useEffect(() => {
        setShowDropDown(false);
    }, [typeOfService]);

    return (
        <div className="typeOfService">
            <h3>Тип услуги</h3>
            <div
                className="select-transportFilter" //сделать наверное общий класс для всех выпадающих
                onClick={() => setShowDropDown(!showDropDown)}
            >
                {typeOfService || 'Не выбрано'}
                {showDropDown ? (
                    <ArrowTop color="#1C1C1E" />
                ) : (
                    <ArrowDown color="#1C1C1E" />
                )}
            </div>
            {showDropDown && (
                // <div className="select-transportFilter-dropdown">
                <div className="select-settingFormFilter-dropdown-height-limited">
                    {arrOfValues.map((el) => (
                        <label key={el}>
                            <input
                                type="radio"
                                value={el}
                                {...register('typeOfService')}
                            />
                            {el}
                            {typeOfService === el && <Jackdaw />}
                        </label>
                    ))}
                </div>
            )}
        </div>
    );
};
