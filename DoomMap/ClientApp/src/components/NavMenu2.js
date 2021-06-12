import React from 'react';
import { Link } from "react-router-dom";
import { fade, makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import SvgIcon from '@material-ui/core/SvgIcon';
import HomeOutlinedIcon from '@material-ui/icons/HomeOutlined';
import HomeWorkOutlinedIcon from '@material-ui/icons/HomeWorkOutlined';
import TimelineOutlinedIcon from '@material-ui/icons/TimelineOutlined';
import FlashOnOutlinedIcon from '@material-ui/icons/FlashOnOutlined';
import MoreIcon from '@material-ui/icons/MoreVert';

const useStyles = makeStyles(theme => ({
    grow: {
        flexGrow: 1,
    },
    topappbar: {
        height: '28px',
        minHeight: '28px',
        backgroundColor: '#babfc7',
        color: '#fff'
    },
    toptoolbar: {
        height: '28px',
        minHeight: '28px',
        padding: 0,
    },
    appbar: {
        height: '78px',
        minHeight: '78px',
        backgroundColor: '#343a40',
        color: '#f8f8f8'
    },
    bottomtoolbar: {
        padding: 0,
        height: '78px',
        minHeight: '78px',
    },
    menuButton: {
        margin: 0,
        padding: 0
    },
    leftlinks: {
        color: '#adb5bd',
        fontSize: '16px',
        padding: '6px 7px',
    },
    rightlinks: {
        color: '#adb5bd',
        fontSize: '14px',
        paddingRight: '5px',
        paddingLeft: '5px'
    },
    title: {
        display: 'block',
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        marginRight: theme.spacing(2),
        marginLeft: 0,
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            marginLeft: theme.spacing(3),
            width: 'auto',
        },
    },
    meckIcon: {
        height: '60px',
        margin: '8px 0px 8px 8px',
    },
    stormwaterIcon: {
        height: '40px',
        margin: '8px',
        padding: '0'
    },
    searchIcon: {
        width: theme.spacing(7),
        height: '100%',
        position: 'absolute',
        pointerEvents: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    inputRoot: {
        color: 'inherit',
    },
    inputInput: {
        padding: theme.spacing(1, 1, 1, 7),
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('md')]: {
            width: 200,
        },
    },
    sectionDesktop: {
        display: 'none',
        [theme.breakpoints.up('md')]: {
            display: 'flex',
        },
    },
    sectionMobile: {
        display: 'flex',
        [theme.breakpoints.up('md')]: {
            display: 'none',
        },
    },
    mobileIcon: {
        color: '#003d59',
        marginRight: '5px',
        marginBottom: '2px'
    },
    mobileLink: {
        color: '#003d59',
        fontWeight: '600',

    }
}));

export default function NavMenu() {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
    const [mobileMoreAnchorEl, setMobileMoreAnchorEl] = React.useState(null);

    const isMenuOpen = Boolean(anchorEl);
    const isMobileMenuOpen = Boolean(mobileMoreAnchorEl);


    const handleMobileMenuClose = () => {
        setMobileMoreAnchorEl(null);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
        handleMobileMenuClose();
    };

    const handleMobileMenuOpen = event => {
        setMobileMoreAnchorEl(event.currentTarget);
    };

    const menuId = 'primary-search-account-menu';
    const renderMenu = (
        <Menu
            anchorEl={anchorEl}
            anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
            id={menuId}
            keepMounted
            transformOrigin={{ vertical: 'top', horizontal: 'right' }}
            open={isMenuOpen}
            onClose={handleMenuClose}
        >
            <MenuItem onClick={handleMenuClose}>Profile</MenuItem>
            <MenuItem onClick={handleMenuClose}>My account</MenuItem>
        </Menu>
    );

    const mobileMenuId = 'primary-search-account-menu-mobile';
    const renderMobileMenu = (
        <Menu
            anchorEl={mobileMoreAnchorEl}
            anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
            id={mobileMenuId}
            keepMounted
            transformOrigin={{ vertical: 'top', horizontal: 'right' }}
            open={isMobileMenuOpen}
            onClose={handleMobileMenuClose}
        >
            <MenuItem>
                <Link to={"/"} href="/">
                    <SvgIcon className={classes.mobileIcon} > <HomeOutlinedIcon /></SvgIcon ><span className={classes.mobileLink}>HOME</span>
                </Link>
            </MenuItem>
            <MenuItem>
                <Link to={"/counter"} href="/dashboard">
                    <SvgIcon className={classes.mobileIcon} > <HomeWorkOutlinedIcon /></SvgIcon ><span className={classes.mobileLink}>COUNTER</span>
                </Link>
            </MenuItem>
            <MenuItem>
                <Link to={"/performance"} href="/fetch-data">
                    <SvgIcon className={classes.mobileIcon} > <TimelineOutlinedIcon /></SvgIcon><span className={classes.mobileLink}>FETCH DATA</span>
                </Link>
            </MenuItem>
        </Menu>
    );

    return (
        <div className={classes.grow}>
            <AppBar position="static" className={classes.appbar}>
                <Toolbar className={classes.bottomtoolbar}>
                    <IconButton
                        edge="start"
                        className={classes.menuButton}
                        color="inherit"
                        aria-label="open drawer"
                    >
                    </IconButton>
                    <IconButton
                        edge="start"
                        className={classes.menuButton}
                        color="inherit"
                        aria-label="open drawer"
                    >
                    </IconButton>
                    <Link to={"/"} href="/">
                        <Typography className={ classes.leftlinks } variant="h3" noWrap>
                            The Doom Map
                    </Typography>
                    </Link>
                    <div className={classes.grow} />
                    <div className={classes.sectionDesktop}>
                        <Link to={"/"} href="/">Home</Link>
                        <Link to={"/map"} href="/map">Map</Link>
                        <Link to={"/counter"} href="/counter">Counter</Link>
                        <Link to={"/fetch-data"} href="/fetch-data">Fetch Data</Link>
                    </div>
                    <div className={classes.sectionMobile}>
                        <IconButton
                            aria-label="show more"
                            aria-controls={mobileMenuId}
                            aria-haspopup="true"
                            onClick={handleMobileMenuOpen}
                            color="inherit"
                        >
                            <MoreIcon />
                        </IconButton>
                    </div>
                </Toolbar>
            </AppBar>
            {renderMobileMenu}
            {renderMenu}
            {renderMenu}
        </div>
    );
}
