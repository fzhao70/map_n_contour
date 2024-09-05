import numpy as np

def pm25_relative_risk_gemm(exposure, param):
    """
    Calculate the relative risk of premature mortality due to PM2.5 exposure
    exposure: float, PM2.5 exposure ug/m3
    
    GEMM : 
    Global estimates of mortality associated with long-term exposure to outdoor fine particulate matter
    Burnett et al. 2018
    
    Health benefits of on-road transportation pollution control programs in China
    Wang et al. 2020
    
    Reductions in premature deaths from heat and particulate matter air pollution in South Asia, China, and the United States under decarbonization
    Drew et al. 2024
    
    IER :
    Global, regional, and national comparative risk assessment of 84 behavioural, environmental and occupational, and metabolic risks or clusters of risks for 195 countries and territories, 1990-2017
    Lancet 2018
    
    Long-term Fine Particulate Matter Exposure and Nonaccidental and Cause-specific Mortality in a Large National Cohort of Chinese Men
    Yin et al. 2017
    """
    theta_hat, theta_se_hat, alpha_hat, mu_hat, pi_hat = param
    min_exposure = 2.4 / 2
    z = max(0, exposure - min_exposure)
    
    gamma_calc = np.log(1 + z / alpha_hat) / (1 + np.exp((mu_hat - z) / pi_hat))
    risk = np.array([
        np.exp(gamma_calc * (theta_hat - 2 * theta_se_hat)), #hazard_ratio
        np.exp(gamma_calc * (theta_hat - 0 * theta_se_hat)), #hazard_ratio
        np.exp(gamma_calc * (theta_hat + 2 * theta_se_hat)), #hazard_ratio
    ])
    
    return risk