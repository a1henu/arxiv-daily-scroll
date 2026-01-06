---
layout: default
title: Prior-Guided DETR for Ultrasound Nodule Detection
---

# Prior-Guided DETR for Ultrasound Nodule Detection
**arXiv**：[2601.02212v1](https://arxiv.org/abs/2601.02212) · [PDF](https://arxiv.org/pdf/2601.02212.pdf)  
**作者**：Jingjing Wang, Zhuo Xiao, Xinning Yao, Bo Liu, Lijuan Niu, Xiangzhi Bai, Fugen Zhou  

**一句话要点**：提出先验引导DETR框架，用于解决超声结节检测中形状不规则、边界模糊和噪声干扰的挑战。

**关键词**：超声结节检测, 先验知识引导, DETR框架, 多尺度特征融合, 斑点噪声抑制

## 3 点简述
- 核心问题：超声结节检测因形状不规则、边界模糊、尺度变化大和斑点噪声而困难。
- 方法要点：通过空间自适应可变形FFN、多尺度空间-频率特征混合器和密集特征交互机制，渐进式融入几何与结构先验知识。
- 实验或效果：在甲状腺和乳腺超声数据集上优于18种方法，尤其在形态复杂结节检测中表现优异。

## 摘要（原文）

> Accurate detection of ultrasound nodules is essential for the early diagnosis and treatment of thyroid and breast cancers. However, this task remains challenging due to irregular nodule shapes, indistinct boundaries, substantial scale variations, and the presence of speckle noise that degrades structural visibility. To address these challenges, we propose a prior-guided DETR framework specifically designed for ultrasound nodule detection. Instead of relying on purely data-driven feature learning, the proposed framework progressively incorporates different prior knowledge at multiple stages of the network. First, a Spatially-adaptive Deformable FFN with Prior Regularization (SDFPR) is embedded into the CNN backbone to inject geometric priors into deformable sampling, stabilizing feature extraction for irregular and blurred nodules. Second, a Multi-scale Spatial-Frequency Feature Mixer (MSFFM) is designed to extract multi-scale structural priors, where spatial-domain processing emphasizes contour continuity and boundary cues, while frequency-domain modeling captures global morphology and suppresses speckle noise. Furthermore, a Dense Feature Interaction (DFI) mechanism propagates and exploits these prior-modulated features across all encoder layers, enabling the decoder to enhance query refinement under consistent geometric and structural guidance. Experiments conducted on two clinically collected thyroid ultrasound datasets (Thyroid I and Thyroid II) and two public benchmarks (TN3K and BUSI) for thyroid and breast nodules demonstrate that the proposed method achieves superior accuracy compared with 18 detection methods, particularly in detecting morphologically complex nodules.The source code is publicly available at https://github.com/wjj1wjj/Ultrasound-DETR.

