---
layout: default
title: Denoising the Deep Sky: Physics-Based CCD Noise Formation for Astronomical Imaging
---

# Denoising the Deep Sky: Physics-Based CCD Noise Formation for Astronomical Imaging
**arXiv**：[2601.23276v1](https://arxiv.org/abs/2601.23276) · [PDF](https://arxiv.org/pdf/2601.23276.pdf)  
**作者**：Shuhong Liu, Xining Ge, Ziying Gu, Lin Gu, Ziteng Cui, Xuangeng Chu, Jun Liu, Dong Li, Tatsuya Harada  

**一句话要点**：提出基于物理的CCD噪声合成框架，以解决天文成像中噪声数据稀缺和模型可解释性问题。

**关键词**：天文成像去噪, CCD噪声建模, 物理合成框架, 监督学习数据集, 多波段观测

## 3 点简述
- 天文成像在观测约束下受噪声限制，现有校准流程难以处理随机噪声。
- 基于物理模型合成噪声，包括光子散粒噪声、暗电流噪声和宇宙射线异常值。
- 构建多波段真实数据集，支持监督学习评估，提升去噪模型的实用性和可重复性。

## 摘要（原文）

> Astronomical imaging remains noise-limited under practical observing constraints, while standard calibration pipelines mainly remove structured artifacts and leave stochastic noise largely unresolved. Learning-based denoising is promising, yet progress is hindered by scarce paired training data and the need for physically interpretable and reproducible models in scientific workflows. We propose a physics-based noise synthesis framework tailored to CCD noise formation. The pipeline models photon shot noise, photo-response non-uniformity, dark-current noise, readout effects, and localized outliers arising from cosmic-ray hits and hot pixels. To obtain low-noise inputs for synthesis, we average multiple unregistered exposures to produce high-SNR bases. Realistic noisy counterparts synthesized from these bases using our noise model enable the construction of abundant paired datasets for supervised learning. We further introduce a real-world dataset across multi-bands acquired with two twin ground-based telescopes, providing paired raw frames and instrument-pipeline calibrated frames, together with calibration data and stacked high-SNR bases for real-world evaluation.

