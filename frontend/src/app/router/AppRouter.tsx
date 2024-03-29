import { Route, Routes } from 'react-router-dom';
import { Layout } from '../layout';
import { privateRoutes, publicRoutes } from './routes';
import { useAppSelector } from '../store/hooks';
import { ActivateAccount } from '../../pages/activateAccount/ActivateAccount';

export const AppRouter = () => {
    const isAuth = useAppSelector((state) => state.setIsAuth.isAuth);

    const routes = isAuth ? privateRoutes : publicRoutes;

    return (
        <Routes>
            <Route path="/" element={<Layout />}>
                {routes
                    .filter((el) => el.component !== ActivateAccount)
                    .map(({ path, component: Component }) => {
                    return (
                        <Route
                            path={`/${path}`}
                            element={<Component />}
                            key={path}
                        />
                    );
                })}
            </Route>
            <Route path="/">
                {routes
                    .filter((el) => el.component === ActivateAccount)
                    .map(({ path, component: Component }) => {
                    return (
                        <Route
                            path={`/${path}`}
                            element={<Component />}
                            key={path}
                        />
                    );
                })}
            </Route>
        </Routes>
    );
};
