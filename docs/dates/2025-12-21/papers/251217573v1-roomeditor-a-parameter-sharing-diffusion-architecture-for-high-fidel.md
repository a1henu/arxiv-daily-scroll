---
layout: default
title: RoomEditor++: A Parameter-Sharing Diffusion Architecture for High-Fidelity Furniture Synthesis
---

# RoomEditor++: A Parameter-Sharing Diffusion Architecture for High-Fidelity Furniture Synthesis
**arXiv**：[2512.17573v1](https://arxiv.org/abs/2512.17573) · [PDF](https://arxiv.org/pdf/2512.17573.pdf)  
**作者**：Qilong Wang, Xiaofan Ming, Zhenyi Lin, Jinwen Li, Dongwei Ren, Wangmeng Zuo, Qinghua Hu  

**一句话要点**：提出RoomEditor++扩散架构以解决虚拟家具合成的高保真与背景完整性挑战

**关键词**：虚拟家具合成, 扩散模型, 参数共享, 室内场景, 高保真图像生成, 基准数据集

## 3 点简述
- 核心问题：虚拟家具合成缺乏可复现基准，现有方法难以保持高保真与背景完整性。
- 方法要点：采用参数共享双扩散骨干，统一参考与背景图像的特征提取与修复过程。
- 实验或效果：在RoomBench++数据集上验证，优于现有方法，泛化能力强无需任务微调。

## 摘要（原文）

> Virtual furniture synthesis, which seamlessly integrates reference objects into indoor scenes while maintaining geometric coherence and visual realism, holds substantial promise for home design and e-commerce applications. However, this field remains underexplored due to the scarcity of reproducible benchmarks and the limitations of existing image composition methods in achieving high-fidelity furniture synthesis while preserving background integrity. To overcome these challenges, we first present RoomBench++, a comprehensive and publicly available benchmark dataset tailored for this task. It consists of 112,851 training pairs and 1,832 testing pairs drawn from both real-world indoor videos and realistic home design renderings, thereby supporting robust training and evaluation under practical conditions. Then, we propose RoomEditor++, a versatile diffusion-based architecture featuring a parameter-sharing dual diffusion backbone, which is compatible with both U-Net and DiT architectures. This design unifies the feature extraction and inpainting processes for reference and background images. Our in-depth analysis reveals that the parameter-sharing mechanism enforces aligned feature representations, facilitating precise geometric transformations, texture preservation, and seamless integration. Extensive experiments validate that RoomEditor++ is superior over state-of-the-art approaches in terms of quantitative metrics, qualitative assessments, and human preference studies, while highlighting its strong generalization to unseen indoor scenes and general scenes without task-specific fine-tuning. The dataset and source code are available at \url{https://github.com/stonecutter-21/roomeditor}.

