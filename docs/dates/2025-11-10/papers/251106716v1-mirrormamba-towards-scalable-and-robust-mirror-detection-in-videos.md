---
layout: default
title: MirrorMamba: Towards Scalable and Robust Mirror Detection in Videos
---

# MirrorMamba: Towards Scalable and Robust Mirror Detection in Videos
**arXiv**：[2511.06716v1](https://arxiv.org/abs/2511.06716) · [PDF](https://arxiv.org/pdf/2511.06716.pdf)  
**作者**：Rui Song, Jiaying Lin, Rynson W. H. Lau  

**一句话要点**：提出MirrorMamba方法以解决视频镜面检测的性能与鲁棒性问题

**关键词**：视频镜面检测, Mamba模型, 多线索融合, 全局感受野, 线性复杂度, 边界增强

## 3 点简述
- 现有方法依赖单一动态特征，且CNN感受野有限或Transformer计算复杂度高
- 利用多线索融合深度、对应性和光流，并引入Mamba模型提取全局特征
- 在视频和图像基准数据集上实现最先进性能，证明其鲁棒性和泛化能力

## 摘要（原文）

> Video mirror detection has received significant research attention, yet
> existing methods suffer from limited performance and robustness. These
> approaches often over-rely on single, unreliable dynamic features, and are
> typically built on CNNs with limited receptive fields or Transformers with
> quadratic computational complexity. To address these limitations, we propose a
> new effective and scalable video mirror detection method, called MirrorMamba.
> Our approach leverages multiple cues to adapt to diverse conditions,
> incorporating perceived depth, correspondence and optical. We also introduce an
> innovative Mamba-based Multidirection Correspondence Extractor, which benefits
> from the global receptive field and linear complexity of the emerging Mamba
> spatial state model to effectively capture correspondence properties.
> Additionally, we design a Mamba-based layer-wise boundary enforcement decoder
> to resolve the unclear boundary caused by the blurred depth map. Notably, this
> work marks the first successful application of the Mamba-based architecture in
> the field of mirror detection. Extensive experiments demonstrate that our
> method outperforms existing state-of-the-art approaches for video mirror
> detection on the benchmark datasets. Furthermore, on the most challenging and
> representative image-based mirror detection dataset, our approach achieves
> state-of-the-art performance, proving its robustness and generalizability.

