import { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { useAppDispatch } from '../../../../app/store/hooks';
import { InputCheckbox } from './inputsRegistration/inputCheckbox/InputCheckbox';
import { InputEmail } from './inputsRegistration/inputEmail/InputEmail';
import { InputName } from './inputsRegistration/inputName/InputName';
import { InputPassword } from './inputsRegistration/inputPassword/InputPassword';
import { InputRepeatPassword } from './inputsRegistration/inputPassword/InputRepeatPassword';
import { InputPhone } from './inputsRegistration/inputPhone/InputPhone';
import { InputSubmit } from './inputsRegistration/inputSubmit/InputSubmit';
import './libr/formRegistration.scss';
import { AuthRegistration } from './libr/RegistrationTypes';
import { submitRegForm } from './libr/onSubmitRegForm';
import { setLoading } from '../../../../entities/loading/model/setLoadingSlice';
import { resetErrors } from '../../../../features/header/model/modalAuth/reducers/auth';

export const FormRegistration = () => {
    const [showPassword, setShowPassword] = useState(false);
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors, isValid },
        getValues,
    } = useForm<AuthRegistration>({
        mode: 'onChange',
    });

    const dispatch = useAppDispatch();

    const onsubmit: SubmitHandler<AuthRegistration> = async (submitData) => {
        await dispatch(setLoading(true))
        await submitRegForm(submitData, dispatch, reset);
        await dispatch(resetErrors())
        await dispatch(setLoading(false))
    };

    return (
        <form
            className="form-registration"
            onSubmit={handleSubmit(onsubmit)}
            autoComplete="false"
        >
            <InputName errors={errors} register={register} />
            <InputPhone errors={errors} register={register} />
            <InputEmail errors={errors} register={register} />
            <InputPassword
                errors={errors}
                register={register}
                showPassword={showPassword}
                setShowPassword={setShowPassword}
            />
            <InputRepeatPassword
                errors={errors}
                register={register}
                showPassword={showPassword}
                setShowPassword={setShowPassword}
                getValues={getValues}
            />
            <InputCheckbox register={register} errors={errors} />
            <InputSubmit isValid={isValid} />
        </form>
    );
};
