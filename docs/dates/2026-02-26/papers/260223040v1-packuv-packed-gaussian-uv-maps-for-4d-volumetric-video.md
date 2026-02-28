---
layout: default
title: PackUV: Packed Gaussian UV Maps for 4D Volumetric Video
---

# PackUV: Packed Gaussian UV Maps for 4D Volumetric Video
**arXiv**：[2602.23040v1](https://arxiv.org/abs/2602.23040) · [PDF](https://arxiv.org/pdf/2602.23040.pdf)  
**作者**：Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar  

**一句话要点**：提出PackUV以解决4D体视频重建、存储和流媒体兼容性问题

**关键词**：4D体视频, 高斯泼溅, UV图谱, 时间一致性, 视频编码兼容, 多视图数据集

## 3 点简述
- 核心问题：现有高斯泼溅方法在长序列、大运动和遮挡下失效，且不兼容标准视频编码
- 方法要点：引入结构化UV图谱表示，通过流引导高斯标记和视频关键帧优化保持时间一致性
- 实验或效果：在大型数据集PackUV-2B上验证，渲染质量优于基线，支持长达30分钟序列

## 摘要（原文）

> Volumetric videos offer immersive 4D experiences, but remain difficult to reconstruct, store, and stream at scale. Existing Gaussian Splatting based methods achieve high-quality reconstruction but break down on long sequences, temporal inconsistency, and fail under large motions and disocclusions. Moreover, their outputs are typically incompatible with conventional video coding pipelines, preventing practical applications.
>   We introduce PackUV, a novel 4D Gaussian representation that maps all Gaussian attributes into a sequence of structured, multi-scale UV atlas, enabling compact, image-native storage. To fit this representation from multi-view videos, we propose PackUV-GS, a temporally consistent fitting method that directly optimizes Gaussian parameters in the UV domain. A flow-guided Gaussian labeling and video keyframing module identifies dynamic Gaussians, stabilizes static regions, and preserves temporal coherence even under large motions and disocclusions. The resulting UV atlas format is the first unified volumetric video representation compatible with standard video codecs (e.g., FFV1) without losing quality, enabling efficient streaming within existing multimedia infrastructure.
>   To evaluate long-duration volumetric capture, we present PackUV-2B, the largest multi-view video dataset to date, featuring more than 50 synchronized cameras, substantial motion, and frequent disocclusions across 100 sequences and 2B (billion) frames. Extensive experiments demonstrate that our method surpasses existing baselines in rendering fidelity while scaling to sequences up to 30 minutes with consistent quality.

