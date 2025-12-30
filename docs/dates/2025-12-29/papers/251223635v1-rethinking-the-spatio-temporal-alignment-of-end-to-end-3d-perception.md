---
layout: default
title: Rethinking the Spatio-Temporal Alignment of End-to-End 3D Perception
---

# Rethinking the Spatio-Temporal Alignment of End-to-End 3D Perception
**arXiv**：[2512.23635v1](https://arxiv.org/abs/2512.23635) · [PDF](https://arxiv.org/pdf/2512.23635.pdf)  
**作者**：Xiaoyu Li, Peidong Li, Xian Wu, Long Shi, Dedong Liu, Yitao Wu, Jiajia Fu, Dixiao Cui, Lijun Zhao, Lining Sun  

**一句话要点**：提出HAT模块以优化自动驾驶中端到端3D感知的时空对齐问题

**关键词**：时空对齐, 端到端感知, 自动驾驶, 3D目标检测, 多假设解码, 运动建模

## 3 点简述
- 现有方法依赖注意力机制和统一显式运动模型进行对齐，但跨类别和帧的运动状态变化导致对齐效果不佳
- HAT模块通过多假设解码，自适应地从多个显式运动模型生成对齐提议，结合语义和运动线索
- 在nuScenes数据集上，HAT提升3D检测和跟踪性能，增强端到端自动驾驶的感知鲁棒性和规划能力

## 摘要（原文）

> Spatio-temporal alignment is crucial for temporal modeling of end-to-end (E2E) perception in autonomous driving (AD), providing valuable structural and textural prior information. Existing methods typically rely on the attention mechanism to align objects across frames, simplifying the motion model with a unified explicit physical model (constant velocity, etc.). These approaches prefer semantic features for implicit alignment, challenging the importance of explicit motion modeling in the traditional perception paradigm. However, variations in motion states and object features across categories and frames render this alignment suboptimal. To address this, we propose HAT, a spatio-temporal alignment module that allows each object to adaptively decode the optimal alignment proposal from multiple hypotheses without direct supervision. Specifically, HAT first utilizes multiple explicit motion models to generate spatial anchors and motion-aware feature proposals for historical instances. It then performs multi-hypothesis decoding by incorporating semantic and motion cues embedded in cached object queries, ultimately providing the optimal alignment proposal for the target frame. On nuScenes, HAT consistently improves 3D temporal detectors and trackers across diverse baselines. It achieves state-of-the-art tracking results with 46.0% AMOTA on the test set when paired with the DETR3D detector. In an object-centric E2E AD method, HAT enhances perception accuracy (+1.3% mAP, +3.1% AMOTA) and reduces the collision rate by 32%. When semantics are corrupted (nuScenes-C), the enhancement of motion modeling by HAT enables more robust perception and planning in the E2E AD.

