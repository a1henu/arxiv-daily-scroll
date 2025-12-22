---
layout: default
title: UrbanDIFF: A Denoising Diffusion Model for Spatial Gap Filling of Urban Land Surface Temperature Under Dense Cloud Cover
---

# UrbanDIFF: A Denoising Diffusion Model for Spatial Gap Filling of Urban Land Surface Temperature Under Dense Cloud Cover
**arXiv**：[2512.17782v1](https://arxiv.org/abs/2512.17782) · [PDF](https://arxiv.org/pdf/2512.17782.pdf)  
**作者**：Arya Chavoshi, Hassan Dashtian, Naveen Sudharsan, Dev Niyogi  

**一句话要点**：提出UrbanDIFF去噪扩散模型，用于密集云层下城市地表温度的空间填补。

**关键词**：去噪扩散模型, 地表温度重建, 空间填补, 城市热岛监测, 云污染处理

## 3 点简述
- 核心问题：卫星地表温度数据常受云污染，现有方法在连续大缺失下性能下降。
- 方法要点：基于去噪扩散模型，结合城市结构信息，通过像素引导细化确保一致性。
- 实验或效果：在85%云覆盖下，SSIM达0.89，RMSE为1.2K，性能随云密度增加下降较慢。

## 摘要（原文）

> Satellite-derived Land Surface Temperature (LST) products are central to surface urban heat island (SUHI) monitoring due to their consistent grid-based coverage over large metropolitan regions. However, cloud contamination frequently obscures LST observations, limiting their usability for continuous SUHI analysis. Most existing LST reconstruction methods rely on multitemporal information or multisensor data fusion, requiring auxiliary observations that may be unavailable or unreliable under persistent cloud cover. Purely spatial gap-filling approaches offer an alternative, but traditional statistical methods degrade under large or spatially contiguous gaps, while many deep learning based spatial models deteriorate rapidly with increasing missingness.
>   Recent advances in denoising diffusion based image inpainting models have demonstrated improved robustness under high missingness, motivating their adoption for spatial LST reconstruction. In this work, we introduce UrbanDIFF, a purely spatial denoising diffusion model for reconstructing cloud contaminated urban LST imagery. The model is conditioned on static urban structure information, including built-up surface data and a digital elevation model, and enforces strict consistency with revealed cloud free pixels through a supervised pixel guided refinement step during inference.
>   UrbanDIFF is trained and evaluated using NASA MODIS Terra LST data from seven major United States metropolitan areas spanning 2002 to 2025. Experiments using synthetic cloud masks with 20 to 85 percent coverage show that UrbanDIFF consistently outperforms an interpolation baseline, particularly under dense cloud occlusion, achieving SSIM of 0.89, RMSE of 1.2 K, and R2 of 0.84 at 85 percent cloud coverage, while exhibiting slower performance degradation as cloud density increases.

