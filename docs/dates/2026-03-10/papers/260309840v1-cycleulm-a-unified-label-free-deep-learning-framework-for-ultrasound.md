---
layout: default
title: CycleULM: A unified label-free deep learning framework for ultrasound localisation microscopy
---

# CycleULM: A unified label-free deep learning framework for ultrasound localisation microscopy
**arXiv**：[2603.09840v1](https://arxiv.org/abs/2603.09840) · [PDF](https://arxiv.org/pdf/2603.09840.pdf)  
**作者**：Su Yan, Clara Rodrigo Gonzalez, Vincent C. H. Leung, Herman Verinaz-Jadan, Jiakang Chen, Matthieu Toulemonde, Kai Riemer, Jipeng Yan, Clotilde Vié, Qingyuan Tan, Peter D. Weinberg, Pier Luigi Dragotti, Kevin G. Murphy, Meng-Xing Tang  

**一句话要点**：提出CycleULM以解决超声定位显微镜中标签稀缺和仿真-现实域差距问题

**关键词**：超声定位显微镜, 无标签学习, CycleGAN, 微泡定位, 实时处理, 超分辨率成像

## 3 点简述
- 核心问题：超声定位显微镜依赖仿真或标记数据，存在标签稀缺和域差距挑战
- 方法要点：利用CycleGAN实现无标签学习，在真实对比增强超声与简化微泡域间进行物理模拟翻译
- 实验或效果：提升图像对比度达15.3 dB，微泡定位召回率提高40%，实现实时处理18.3帧/秒

## 摘要（原文）

> Super-resolution ultrasound via microbubble (MB) localisation and tracking, also known as ultrasound localisation microscopy (ULM), can resolve microvasculature beyond the acoustic diffraction limit. However, significant challenges remain in localisation performance and data acquisition and processing time. Deep learning methods for ULM have shown promise to address these challenges, however, they remain limited by in vivo label scarcity and the simulation-to-reality domain gap. We present CycleULM, the first unified label-free deep learning framework for ULM. CycleULM learns a physics-emulating translation between the real contrast-enhanced ultrasound (CEUS) data domain and a simplified MB-only domain, leveraging the power of CycleGAN without requiring paired ground truth data. With this translation, CycleULM removes dependence on high-fidelity simulators or labelled data, and makes MB localisation and tracking substantially easier. Deployed as modular plug-and-play components within existing pipelines or as an end-to-end processing framework, CycleULM delivers substantial performance gains across both in silico and in vivo datasets. Specifically, CycleULM improves image contrast (contrast-to-noise ratio) by up to 15.3 dB and sharpens CEUS resolution with a 2.5{\times} reduction in the full width at half maximum of the point spread function. CycleULM also improves MB localisation performance, with up to +40% recall, +46% precision, and a -14.0 μm mean localisation error, yielding more faithful vascular reconstructions. Importantly, CycleULM achieves real-time processing throughput at 18.3 frames per second with order-of-magnitude speed-ups (up to ~14.5{\times}). By combining label-free learning, performance enhancement, and computational efficiency, CycleULM provides a practical pathway toward robust, real-time ULM and accelerates its translation to clinical applications.

