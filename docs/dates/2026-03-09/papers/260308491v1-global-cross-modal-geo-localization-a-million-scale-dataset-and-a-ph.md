---
layout: default
title: Global Cross-Modal Geo-Localization: A Million-Scale Dataset and a Physical Consistency Learning Framework
---

# Global Cross-Modal Geo-Localization: A Million-Scale Dataset and a Physical Consistency Learning Framework
**arXiv**：[2603.08491v1](https://arxiv.org/abs/2603.08491) · [PDF](https://arxiv.org/pdf/2603.08491.pdf)  
**作者**：Yutong Hu, Jinhui Chen, Chaoqiang Xu, Yuan Kou, Sili Zhou, Shaocheng Yan, Pengcheng Shi, Qingwu Hu, Jiayuan Li  

**一句话要点**：提出百万级数据集CORE与物理一致性学习框架PLANET，以解决全球跨模态地理定位中场景多样性不足的问题。

**关键词**：跨模态地理定位, 百万级数据集, 物理一致性学习, 对比学习, 大视觉语言模型, 全球尺度定位

## 3 点简述
- 现有跨模态地理定位研究受限于地理覆盖范围窄、场景多样性不足，难以反映全球建筑风格与地形特征的巨大空间异质性。
- 引入首个百万级全球跨模态地理定位数据集CORE，并利用大视觉语言模型合成高质量场景描述；提出物理定律感知网络PLANET，通过对比学习引导文本表征捕获卫星图像的物理特征。
- 在多个地理区域的广泛实验中，PLANET显著优于现有最先进方法，为鲁棒的全球尺度地理定位建立了新基准。

## 摘要（原文）

> Cross-modal Geo-localization (CMGL) matches ground-level text descriptions with geo-tagged aerial imagery, which is crucial for pedestrian navigation and emergency response. However, existing researches are constrained by narrow geographic coverage and simplistic scene diversity, failing to reflect the immense spatial heterogeneity of global architectural styles and topographic features. To bridge this gap and facilitate universal positioning, we introduce CORE, the first million-scale dataset dedicated to global CMGL. CORE comprises 1,034,786 cross-view images sampled from 225 distinct geographic regions across all continents, offering an unprecedented variety of perspectives in varying environmental conditions and urban layouts. We leverage the zero-shot reasoning of Large Vision-Language Models (LVLMs) to synthesize high-quality scene descriptions rich in discriminative cues. Furthermore, we propose a physical-law-aware network (PLANET) for cross-modal geo-localization. PLANET introduces a novel contrastive learning paradigm to guide textual representations in capturing the intrinsic physical signatures of satellite imagery. Extensive experiments across varied geographic regions demonstrate that PLANet significantly outperforms state-of-the-art methods, establishing a new benchmark for robust, global-scale geo-localization. The dataset and source code will be released at https://github.com/YtH0823/CORE.

