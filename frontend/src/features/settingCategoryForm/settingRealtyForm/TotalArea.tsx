import { UseFormRegister } from 'react-hook-form';
import { TypeSettingRealty } from 'widgets/settingForm/settingRealty/libr/TypeSettingRealty';

interface Props {
    register: UseFormRegister<TypeSettingRealty>;
}

export const TotalArea = ({ register }: Props) => {
    return (
        <div className="total-area">
            <h3>Общая площадь, м2</h3>
            <div className="total-area-inputs">
                <input
                    id="total-area-input-min"
                    type="number"
                    placeholder="От"
                    {...register('totalArea.min')}
                />
                <input
                    id="total-area-input-max"
                    type="number"
                    placeholder="До"
                    {...register('totalArea.max')}
                />
            </div>
        </div>
    );
};
