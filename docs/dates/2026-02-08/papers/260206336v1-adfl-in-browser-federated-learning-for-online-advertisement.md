---
layout: default
title: AdFL: In-Browser Federated Learning for Online Advertisement
---

# AdFL: In-Browser Federated Learning for Online Advertisement
**arXiv**：[2602.06336v1](https://arxiv.org/abs/2602.06336) · [PDF](https://arxiv.org/pdf/2602.06336.pdf)  
**作者**：Ahmad Alemari, Pritam Sen, Cristian Borcea  

**一句话要点**：提出AdFL框架，在浏览器中实现联邦学习以平衡在线广告定向与用户隐私。

**关键词**：联邦学习, 在线广告, 浏览器内学习, 用户隐私, 差分隐私, 广告可见性预测

## 3 点简述
- 核心问题：在线出版商需在定向广告收入与用户隐私（如GDPR）间取得平衡。
- 方法要点：AdFL在浏览器中分布式学习用户广告偏好，无需安装软件，利用标准API。
- 实验或效果：原型测试显示，广告可见性预测AUC达92.59%，差分隐私保护下性能适度下降。

## 摘要（原文）

> Since most countries are coming up with online privacy regulations, such as GDPR in the EU, online publishers need to find a balance between revenue from targeted advertisement and user privacy. One way to be able to still show targeted ads, based on user personal and behavioral information, is to employ Federated Learning (FL), which performs distributed learning across users without sharing user raw data with other stakeholders in the publishing ecosystem. This paper presents AdFL, an FL framework that works in the browsers to learn user ad preferences. These preferences are aggregated in a global FL model, which is then used in the browsers to show more relevant ads to users. AdFL can work with any model that uses features available in the browser such as ad viewability, ad click-through, user dwell time on pages, and page content. The AdFL server runs at the publisher and coordinates the learning process for the users who browse pages on the publisher's website. The AdFL prototype does not require the client to install any software, as it is built utilizing standard APIs available on most modern browsers. We built a proof-of-concept model for ad viewability prediction that runs on top of AdFL. We tested AdFL and the model with two non-overlapping datasets from a website with 40K visitors per day. The experiments demonstrate AdFL's feasibility to capture the training information in the browser in a few milliseconds, show that the ad viewability prediction achieves up to 92.59% AUC, and indicate that utilizing differential privacy (DP) to safeguard local model parameters yields adequate performance, with only modest declines in comparison to the non-DP variant.

