import { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { ResetPasswordType } from './libr/types';
import { InputPassword } from './inputs/InputPassword';
import { InputRepeatPassword } from './inputs/InputRepeatPassword';
import { InputSubmit } from './inputs/InputSubmit';
import { confimResetPassword } from './api/confirmResetPassword';
import { NavLink, useParams } from 'react-router-dom';
import { useAppDispatch, useAppSelector } from '../../app/store/hooks';
import { Dispatch } from '@reduxjs/toolkit';
import { setLoading } from '../../entities/loading/model/setLoadingSlice';
import { LoadingWithBackground } from '../../entities/loading/LoadingWithBackground';

export const FormConfirmResetPassword = () => {
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
    const dispatch: Dispatch = useAppDispatch()
    const load = useAppSelector((state) => state.setLoading.loading)

    const onsubmit: SubmitHandler<ResetPasswordType> = async (submitData) => {
        if (uid && token) {
            await dispatch(setLoading(true))

            const response = await confimResetPassword({
                new_password: submitData.password,
                uid,
                token,
            });
            if (response.ok){
                await setSuccess(true);
                await dispatch(setLoading(false))
            }
        }
    };

    return (
        <div className="reset">
            {load && <LoadingWithBackground />}
            {!success ? (
                <form
                    className="form"
                    onSubmit={handleSubmit(onsubmit)}
                    autoComplete="false"
                >
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
                <div className="reset-success">
                    Ваш пароль был успешно изменён!
                    <NavLink className="main-link" to={'/'}>
                        Вернуться на главную
                    </NavLink>
                </div>
            )}
        </div>
    );
};
