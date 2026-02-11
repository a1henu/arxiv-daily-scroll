---
layout: default
title: Allure of Craquelure: A Variational-Generative Approach to Crack Detection in Paintings
---

# Allure of Craquelure: A Variational-Generative Approach to Crack Detection in Paintings
**arXiv**：[2602.09730v1](https://arxiv.org/abs/2602.09730) · [PDF](https://arxiv.org/pdf/2602.09730.pdf)  
**作者**：Laura Paul, Holger Rauhut, Martin Burger, Samira Kabri, Tim Roith  

**一句话要点**：提出变分-生成混合方法以解决绘画中裂纹检测的挑战

**关键词**：裂纹检测, 变分方法, 生成模型, 艺术品分析, 逆问题

## 3 点简述
- 核心问题：绘画中裂纹与艺术特征视觉相似，自动化检测困难
- 方法要点：将裂纹检测建模为逆问题，结合生成模型和变分函数分解图像
- 实验或效果：通过联合优化生成像素级裂纹定位图，支持艺术品保护

## 摘要（原文）

> Recent advances in imaging technologies, deep learning and numerical performance have enabled non-invasive detailed analysis of artworks, supporting their documentation and conservation. In particular, automated detection of craquelure in digitized paintings is crucial for assessing degradation and guiding restoration, yet remains challenging due to the possibly complex scenery and the visual similarity between cracks and crack-like artistic features such as brush strokes or hair. We propose a hybrid approach that models crack detection as an inverse problem, decomposing an observed image into a crack-free painting and a crack component. A deep generative model is employed as powerful prior for the underlying artwork, while crack structures are captured using a Mumford--Shah-type variational functional together with a crack prior. Joint optimization yields a pixel-level map of crack localizations in the painting.

