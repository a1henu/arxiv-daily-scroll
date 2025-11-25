---
layout: default
title: MFmamba: A Multi-function Network for Panchromatic Image Resolution Restoration Based on State-Space Model
---

# MFmamba: A Multi-function Network for Panchromatic Image Resolution Restoration Based on State-Space Model
**arXiv**：[2511.18888v1](https://arxiv.org/abs/2511.18888) · [PDF](https://arxiv.org/pdf/2511.18888.pdf)  
**作者**：Qian Jiang, Qianqian Wang, Xin Jin, Michal Wozniak, Shaowen Yao, Wei Zhou  

**一句话要点**：提出MFmamba网络，基于状态空间模型实现全色图像分辨率恢复与光谱恢复

**关键词**：遥感图像处理, 超分辨率, 光谱恢复, 状态空间模型, 多任务学习

## 3 点简述
- 核心问题：仅输入高空间分辨率灰度全色图像时，如何同时提升空间与光谱分辨率
- 方法要点：结合UNet++与Mamba上采样块，设计双池注意力和多尺度混合交叉块
- 实验或效果：在多个任务中评估指标和视觉结果具有竞争力，仅需单输入

## 摘要（原文）

> Remote sensing images are becoming increasingly widespread in military, earth resource exploration. Because of the limitation of a single sensor, we can obtain high spatial resolution grayscale panchromatic (PAN) images and low spatial resolution color multispectral (MS) images. Therefore, an important issue is to obtain a color image with high spatial resolution when there is only a PAN image at the input. The existing methods improve spatial resolution using super-resolution (SR) technology and spectral recovery using colorization technology. However, the SR technique cannot improve the spectral resolution, and the colorization technique cannot improve the spatial resolution. Moreover, the pansharpening method needs two registered inputs and can not achieve SR. As a result, an integrated approach is expected. To solve the above problems, we designed a novel multi-function model (MFmamba) to realize the tasks of SR, spectral recovery, joint SR and spectral recovery through three different inputs. Firstly, MFmamba utilizes UNet++ as the backbone, and a Mamba Upsample Block (MUB) is combined with UNet++. Secondly, a Dual Pool Attention (DPA) is designed to replace the skip connection in UNet++. Finally, a Multi-scale Hybrid Cross Block (MHCB) is proposed for initial feature extraction. Many experiments show that MFmamba is competitive in evaluation metrics and visual results and performs well in the three tasks when only the input PAN image is used.

