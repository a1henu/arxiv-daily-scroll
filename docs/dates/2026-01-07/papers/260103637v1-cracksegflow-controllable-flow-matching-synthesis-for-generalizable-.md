---
layout: default
title: CrackSegFlow: Controllable Flow-Matching Synthesis for Generalizable Crack Segmentation with the CSF-50K Benchmark
---

# CrackSegFlow: Controllable Flow-Matching Synthesis for Generalizable Crack Segmentation with the CSF-50K Benchmark
**arXiv**：[2601.03637v1](https://arxiv.org/abs/2601.03637) · [PDF](https://arxiv.org/pdf/2601.03637.pdf)  
**作者**：Babak Asadi, Peiyang Wu, Mani Golparvar-Fard, Ramez Hajj  

**一句话要点**：提出CrackSegFlow可控流匹配合成框架，以解决裂缝分割中标签稀缺和域偏移问题。

**关键词**：裂缝分割, 流匹配合成, 域泛化, 可控生成, 数据集基准, 图像合成

## 3 点简述
- 核心问题：裂缝分割面临像素级标签稀缺和传感器、光照等域偏移，限制实际部署。
- 方法要点：通过可控流匹配合成生成逼真裂缝图像和掩码，保持严格对齐，并注入背景以多样化数据。
- 实验或效果：在多个基准测试中提升性能，跨域合成平均增益显著，并发布CSF-50K数据集用于大规模基准测试。

## 摘要（原文）

> Automated crack segmentation is essential for scalable condition assessment of pavements and civil infrastructure, yet practical deployment is limited by scarce pixel-level labels and severe domain shift across sensors, illumination, textures, and annotation conventions. This paper presents CrackSegFlow, a controllable flow-matching synthesis framework that generates photorealistic crack images conditioned on binary masks while preserving strict mask-image alignment. The generator combines topology-preserving mask injection with boundary-gated modulation to maintain thin-structure continuity and suppress texture-driven false positives. A second class-conditional flow-matching model synthesizes crack masks with explicit control over crack coverage, enabling balanced, topology-diverse paired data without additional manual annotation. We further inject crack masks into crack-free backgrounds to diversify illumination and surface artifacts and reduce false positives caused by shadows, joints, and pavement markings. Experiments on five benchmarks spanning four asphalt datasets and the crack class of a concrete-domain dataset demonstrate consistent improvements under an established hybrid CNN--Transformer segmentation backbone and a fixed training protocol. With real plus synthesized pairs, in-domain performance improves on average by 5.37 mIoU and 5.13 F1, and target-guided cross-domain synthesis yields average gains of 13.12 mIoU and 14.82 F1 using only limited target mask statistics. Compared with diffusion-based semantic synthesis, CrackSegFlow provides substantially faster deterministic sampling and improves fidelity and mask-image alignment for thin-structure crack geometry. Finally, we release CSF-50K, a public dataset of 50,000 paired crack images and pixel-accurate masks for large-scale benchmarking of generalizable crack segmentation.

