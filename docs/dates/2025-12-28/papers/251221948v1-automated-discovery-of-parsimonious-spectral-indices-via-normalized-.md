---
layout: default
title: Automated Discovery of Parsimonious Spectral Indices via Normalized Difference Polynomials
---

# Automated Discovery of Parsimonious Spectral Indices via Normalized Difference Polynomials
**arXiv**：[2512.21948v1](https://arxiv.org/abs/2512.21948) · [PDF](https://arxiv.org/pdf/2512.21948.pdf)  
**作者**：Ali Lotfi, Adam Carter, Thuan Ha, Mohammad Meysami, Kwabena Nketia, Steve Shirtliffe  

**一句话要点**：提出基于归一化差分多项式的自动化方法，以发现紧凑光谱指数用于植被分类。

**关键词**：光谱指数, 植被分类, 特征选择, 归一化差分, 遥感分析, 自动化发现

## 3 点简述
- 核心问题：自动化发现紧凑光谱指数以提升植被分类的准确性和可解释性。
- 方法要点：构建归一化差分多项式组合，结合特征选择方法筛选出少量高精度指数。
- 实验或效果：在Sentinel-2影像上测试，单个指数达到96.26%准确率，验证了方法的有效性。

## 摘要（原文）

> We introduce an automated way to find compact spectral indices for vegetation classification. The idea is to take all pairwise normalized differences from the spectral bands and then build polynomial combinations up to a fixed degree, which gives a structured search space that still keeps the illumination invariance needed in remote sensing. For a sensor with $n$ bands this produces $\binom{n}{2}$ base normalized differences, and the degree-2 polynomial expansion gives 1,080 candidate features for the 10-band Sentinel-2 configuration we use here. Feature selection methods (ANOVA filtering, recursive elimination, and $L_1$-regularized SVM) then pick out small sets of indices that reach the desired accuracy, so the final models stay simple and easy to interpret. We test the framework on Kochia (\textit{Bassia scoparia}) detection using Sentinel-2 imagery from Saskatchewan, Canada ($N = 2{,}318$ samples, 2022--2024). A single degree-2 index, the product of two normalized differences from the red-edge bands, already reaches 96.26\% accuracy, and using eight indices only raises this to 97.70\%. In every case the chosen features are degree-2 products built from bands $b_4$ through $b_8$, which suggests that the discriminative signal comes from spectral \emph{interactions} rather than individual band ratios. Because the indices involve only simple arithmetic, they can be deployed directly in platforms like Google Earth Engine. The same approach works for other sensors and classification tasks, and an open-source implementation (\texttt{ndindex}) is available.

