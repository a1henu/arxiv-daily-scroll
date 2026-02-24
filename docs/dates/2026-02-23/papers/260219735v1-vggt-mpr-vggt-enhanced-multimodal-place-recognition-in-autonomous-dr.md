---
layout: default
title: VGGT-MPR: VGGT-Enhanced Multimodal Place Recognition in Autonomous Driving Environments
---

# VGGT-MPR: VGGT-Enhanced Multimodal Place Recognition in Autonomous Driving Environments
**arXiv**：[2602.19735v1](https://arxiv.org/abs/2602.19735) · [PDF](https://arxiv.org/pdf/2602.19735.pdf)  
**作者**：Jingyi Xu, Zhangshuo Qi, Zhongmiao Yan, Xuyu Gao, Qianyun Jiao, Songpengcheng Xia, Xieyuanli Chen, Ling Pei  

**一句话要点**：提出VGGT-MPR框架，利用VGGT增强自动驾驶环境中的多模态地点识别

**关键词**：多模态地点识别, 自动驾驶, 视觉几何基础变换器, 深度感知监督, 训练无关重排序, 全局检索

## 3 点简述
- 核心问题：现有多模态地点识别方法依赖手工融合策略和重训练，效率低且参数多
- 方法要点：采用VGGT作为统一几何引擎，结合深度感知监督和训练无关重排序机制
- 实验或效果：在大规模基准和自采数据上实现先进性能，对环境和视角变化鲁棒

## 摘要（原文）

> In autonomous driving, robust place recognition is critical for global localization and loop closure detection. While inter-modality fusion of camera and LiDAR data in multimodal place recognition (MPR) has shown promise in overcoming the limitations of unimodal counterparts, existing MPR methods basically attend to hand-crafted fusion strategies and heavily parameterized backbones that require costly retraining. To address this, we propose VGGT-MPR, a multimodal place recognition framework that adopts the Visual Geometry Grounded Transformer (VGGT) as a unified geometric engine for both global retrieval and re-ranking. In the global retrieval stage, VGGT extracts geometrically-rich visual embeddings through prior depth-aware and point map supervision, and densifies sparse LiDAR point clouds with predicted depth maps to improve structural representation. This enhances the discriminative ability of fused multimodal features and produces global descriptors for fast retrieval. Beyond global retrieval, we design a training-free re-ranking mechanism that exploits VGGT's cross-view keypoint-tracking capability. By combining mask-guided keypoint extraction with confidence-aware correspondence scoring, our proposed re-ranking mechanism effectively refines retrieval results without additional parameter optimization. Extensive experiments on large-scale autonomous driving benchmarks and our self-collected data demonstrate that VGGT-MPR achieves state-of-the-art performance, exhibiting strong robustness to severe environmental changes, viewpoint shifts, and occlusions. Our code and data will be made publicly available.

