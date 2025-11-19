---
layout: default
title: Segmentation-Aware Latent Diffusion for Satellite Image Super-Resolution: Enabling Smallholder Farm Boundary Delineation
---

# Segmentation-Aware Latent Diffusion for Satellite Image Super-Resolution: Enabling Smallholder Farm Boundary Delineation
**arXiv**：[2511.14481v1](https://arxiv.org/abs/2511.14481) · [PDF](https://arxiv.org/pdf/2511.14481.pdf)  
**作者**：Aditi Agarwal, Anjali Jain, Nikita Saxena, Ishan Deshpande, Michal Kazmierski, Abigail Annkah, Nadav Sherman, Karthikeyan Shanmugam, Alok Talekar, Vaibhav Rajan  

**一句话要点**：提出SEED-SR方法，在分割感知潜在空间进行超分，以支持小农户农场边界描绘

**关键词**：卫星图像超分辨率, 潜在扩散模型, 农场边界分割, 参考图像超分, 多源地理空间数据

## 3 点简述
- 小农户农场边界分割需高分辨率图像，但高分辨率图像重访频率低，难以满足季节性监测需求
- SEED-SR结合条件潜在扩散模型与地理空间基础模型，在潜在空间直接生成分割图，避免像素空间超分
- 实验显示，在20倍尺度因子下，实例和语义分割指标相对提升达25.5%和12.9%

## 摘要（原文）

> Delineating farm boundaries through segmentation of satellite images is a fundamental step in many agricultural applications. The task is particularly challenging for smallholder farms, where accurate delineation requires the use of high resolution (HR) imagery which are available only at low revisit frequencies (e.g., annually). To support more frequent (sub-) seasonal monitoring, HR images could be combined as references (ref) with low resolution (LR) images -- having higher revisit frequency (e.g., weekly) -- using reference-based super-resolution (Ref-SR) methods. However, current Ref-SR methods optimize perceptual quality and smooth over crucial features needed for downstream tasks, and are unable to meet the large scale-factor requirements for this task. Further, previous two-step approaches of SR followed by segmentation do not effectively utilize diverse satellite sources as inputs. We address these problems through a new approach, $\textbf{SEED-SR}$, which uses a combination of conditional latent diffusion models and large-scale multi-spectral, multi-source geo-spatial foundation models. Our key innovation is to bypass the explicit SR task in the pixel space and instead perform SR in a segmentation-aware latent space. This unique approach enables us to generate segmentation maps at an unprecedented 20$\times$ scale factor, and rigorous experiments on two large, real datasets demonstrate up to $\textbf{25.5}$ and $\textbf{12.9}$ relative improvement in instance and semantic segmentation metrics respectively over approaches based on state-of-the-art Ref-SR methods.

