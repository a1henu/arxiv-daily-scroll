---
layout: default
title: TempDiffReg: Temporal Diffusion Model for Non-Rigid 2D-3D Vascular Registration
---

# TempDiffReg: Temporal Diffusion Model for Non-Rigid 2D-3D Vascular Registration
**arXiv**：[2601.18168v1](https://arxiv.org/abs/2601.18168) · [PDF](https://arxiv.org/pdf/2601.18168.pdf)  
**作者**：Zehua Liu, Shihao Zou, Jincai Huang, Yanfang Zhang, Chao Tong, Weixin Si  

**一句话要点**：提出TempDiffReg，一种基于时序扩散模型的非刚性2D-3D血管配准方法，用于辅助经动脉化疗栓塞术。

**关键词**：血管配准, 时序扩散模型, 非刚性配准, 经动脉化疗栓塞术, 2D-3D配准

## 3 点简述
- 核心问题：经动脉化疗栓塞术中血管导航复杂，需准确2D-3D血管配准以指导器械定位。
- 方法要点：采用由粗到精策略，先全局对齐模块SA-PnP建立对应，再时序扩散模型迭代变形捕获解剖变化。
- 实验或效果：在23名患者数据上评估，MSE为0.63毫米，比现有方法降低66.7%，提升配准准确性和解剖合理性。

## 摘要（原文）

> Transarterial chemoembolization (TACE) is a preferred treatment option for hepatocellular carcinoma and other liver malignancies, yet it remains a highly challenging procedure due to complex intra-operative vascular navigation and anatomical variability. Accurate and robust 2D-3D vessel registration is essential to guide microcatheter and instruments during TACE, enabling precise localization of vascular structures and optimal therapeutic targeting. To tackle this issue, we develop a coarse-to-fine registration strategy. First, we introduce a global alignment module, structure-aware perspective n-point (SA-PnP), to establish correspondence between 2D and 3D vessel structures. Second, we propose TempDiffReg, a temporal diffusion model that performs vessel deformation iteratively by leveraging temporal context to capture complex anatomical variations and local structural changes. We collected data from 23 patients and constructed 626 paired multi-frame samples for comprehensive evaluation. Experimental results demonstrate that the proposed method consistently outperforms state-of-the-art (SOTA) methods in both accuracy and anatomical plausibility. Specifically, our method achieves a mean squared error (MSE) of 0.63 mm and a mean absolute error (MAE) of 0.51 mm in registration accuracy, representing 66.7\% lower MSE and 17.7\% lower MAE compared to the most competitive existing approaches. It has the potential to assist less-experienced clinicians in safely and efficiently performing complex TACE procedures, ultimately enhancing both surgical outcomes and patient care. Code and data are available at: \textcolor{blue}{https://github.com/LZH970328/TempDiffReg.git}

