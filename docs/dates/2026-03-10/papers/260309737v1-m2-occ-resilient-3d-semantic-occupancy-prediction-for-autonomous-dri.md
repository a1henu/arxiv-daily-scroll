---
layout: default
title: $M^2$-Occ: Resilient 3D Semantic Occupancy Prediction for Autonomous Driving with Incomplete Camera Inputs
---

# $M^2$-Occ: Resilient 3D Semantic Occupancy Prediction for Autonomous Driving with Incomplete Camera Inputs
**arXiv**：[2603.09737v1](https://arxiv.org/abs/2603.09737) · [PDF](https://arxiv.org/pdf/2603.09737.pdf)  
**作者**：Kaixin Lin, Kunyu Peng, Di Wen, Yufan Chen, Ruiping Liu, Kailun Yang  

**一句话要点**：提出M²-Occ框架以解决自动驾驶中相机输入不完整时的3D语义占据预测问题

**关键词**：3D语义占据预测, 自动驾驶感知, 多视图融合, 特征恢复, 语义一致性, 鲁棒性评估

## 3 点简述
- 核心问题：现有相机方法假设完整环视输入，但实际部署中常因遮挡或故障导致视图缺失
- 方法要点：通过多视图掩码重建模块恢复缺失视图特征，并利用特征记忆模块集成全局语义先验
- 实验或效果：在nuScenes基准上，缺失后视图时IoU提升4.93%，五视图缺失时提升5.01%，且不影响全视图性能

## 摘要（原文）

> Semantic occupancy prediction enables dense 3D geometric and semantic understanding for autonomous driving. However, existing camera-based approaches implicitly assume complete surround-view observations, an assumption that rarely holds in real-world deployment due to occlusion, hardware malfunction, or communication failures. We study semantic occupancy prediction under incomplete multi-camera inputs and introduce $M^2$-Occ, a framework designed to preserve geometric structure and semantic coherence when views are missing. $M^2$-Occ addresses two complementary challenges. First, a Multi-view Masked Reconstruction (MMR) module leverages the spatial overlap among neighboring cameras to recover missing-view representations directly in the feature space. Second, a Feature Memory Module (FMM) introduces a learnable memory bank that stores class-level semantic prototypes. By retrieving and integrating these global priors, the FMM refines ambiguous voxel features, ensuring semantic consistency even when observational evidence is incomplete. We introduce a systematic missing-view evaluation protocol on the nuScenes-based SurroundOcc benchmark, encompassing both deterministic single-view failures and stochastic multi-view dropout scenarios. Under the safety-critical missing back-view setting, $M^2$-Occ improves the IoU by 4.93%. As the number of missing cameras increases, the robustness gap further widens; for instance, under the setting with five missing views, our method boosts the IoU by 5.01%. These gains are achieved without compromising full-view performance. The source code will be publicly released at https://github.com/qixi7up/M2-Occ.

