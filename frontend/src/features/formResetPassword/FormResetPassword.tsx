import { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { ResetPasswordType } from './libr/types';
import { InputPassword } from './inputs/InputPassword';
import { InputRepeatPassword } from './inputs/InputRepeatPassword';
import { InputSubmit } from './inputs/InputSubmit';
import { confimResetPassword } from './api/confirmResetPassword';
import { NavLink, useParams } from 'react-router-dom';

export const FormResetPassword = () => {
    const [showPassword, setShowPassword] = useState(false);
    const {
        register,
        handleSubmit,
        formState: { errors, isValid },
        watch,
    } = useForm<ResetPasswordType>({
        mode: 'all',
    });
    const { uid, token } = useParams();
    const [success, setSuccess] = useState<boolean>(false);

    const onsubmit: SubmitHandler<ResetPasswordType> = async (submitData) => {
        if (uid && token) {
            const response = await confimResetPassword({
                new_password: submitData.password,
                uid,
                token,
            });
            if (response.ok) setSuccess(true);
        }
    };

    return (
        <div className="reset">
            {!success ? (
                <form onSubmit={handleSubmit(onsubmit)} autoComplete="false">
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
                        watch={watch}
                    />
                    <InputSubmit isValid={isValid} />
                </form>
            ) : (
                <>
                    Ваш пароль был успешно изменён!
                    <NavLink to={'/'}>Вернуться на главную</NavLink>
                </>
            )}
        </div>
    );
};
