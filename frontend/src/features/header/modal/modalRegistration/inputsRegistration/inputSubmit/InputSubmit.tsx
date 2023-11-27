interface Props {
    isValid: boolean;
}

export const InputSubmit = ({ isValid }: Props) => {
    return (
        <input
            type="submit"
            className="submit"
            value="Зарегистрироваться"
            disabled={!isValid}
        />
    );
};
