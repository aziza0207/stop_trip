import { FieldErrors, UseFormRegister } from 'react-hook-form';
import { AuthRegistration } from '../../libr/RegistrationTypes';

interface Props {
    errors: FieldErrors<AuthRegistration>;
    register: UseFormRegister<AuthRegistration>;
}

export const InputCheckbox = ({ register }: Props) => {
    return (
        <div className="user-agreement">
            <label htmlFor="userAgreement" className="form-checkbox">
                <input
                    id="userAgreement"
                    // style={errors?.agreement ? {borderColor: 'red'} : {}}
                    {...register('agreement', { required: true })}
                    type="checkbox"
                />
                <span>
                    <p>
                        Я принимаю условия{' '}
                        <a
                            href="#"
                            target="_blank"
                            onClick={(event) => event.stopPropagation()}
                            className="user-agreement-text"
                        >
                            Пользовательского соглашения
                        </a>
                    </p>
                </span>
            </label>
        </div>
    );
};
